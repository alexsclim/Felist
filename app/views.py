from app import app, mail, mysql
from flask import Flask, render_template, redirect, url_for, request, flash, session, json
from forms import ContactForm, RegistrationForm, LoginForm, CreateTeamForm, CreateMemberForm, UpdateMemberForm, CreateRegattaForm
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from query_service import QueryService
from functools import wraps
import gc

def login_required(f):
  @wraps(f)
  def check_session(*args, **kwargs):
    if session.get('username') is None:
      return redirect(url_for('login'))
    return f(*args, **kwargs)
  return check_session

@app.route('/debug', methods=['GET'])
def debug():
  cur = mysql.connection.cursor()
  query_service = QueryService(cur)
  print()
  return render_template('dashboard.html')

@app.route('/', methods=['GET'])
def index():
  if session.get('logged_in') is None:
    return redirect(url_for('login'))
  else:
    return redirect(url_for('dashboard'))

@app.route('/regattas', methods=['GET', 'POST'])
@login_required
def regattas():

  cur = mysql.connection.cursor()
  query_service = QueryService(cur)

  fastest_avg = query_service.fastest_avg_race()

  if request.method == "POST":
    if 'Search Regattas' in request.form.values():
      search = request.form['search-input']
      regattas = query_service.search_regattas(search)
    elif 'Find Regattas With All Teams From This Region' in request.form.values():
      search = request.form['selected-province']
      regattas = query_service.search_regattas_with_all_teams_from_province(search)
    elif 'Clear Search' in request.form.values():
      regattas = query_service.get_regattas()
  else:
    regattas = query_service.get_regattas()

  provinces = query_service.get_distinct_provinces()
  return render_template('regattas.html', regattas=regattas, provinces=provinces, fastest_avg = fastest_avg)

@app.route('/regattas/<regatta_id>/delete', methods=['POST'])
@login_required
def delete_regatta(regatta_id):
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)

  query_service.delete_regatta(conn, regatta_id)
  flash("Regatta was deleted!")
  return redirect(url_for('regattas'))

@app.route('/teams', methods=['GET', 'POST'])
@login_required
def teams():

  cur = mysql.connection.cursor()
  query_service = QueryService(cur)

  avg_members = query_service.avg_members_per_team()
  fastest_avg_time = query_service.fastest_avg_team()


  if request.method == "POST":
    if 'Search Team' in request.form.values():
      search = request.form['search-input']
      teams = query_service.search_teams(search)

      return render_template('teams.html', teams=teams, avg=avg_members, fastest_avg = fastest_avg_time)
    if 'Clear Search' in request.form.values():
      teams = query_service.get_teams()

      return render_template('teams.html', teams=teams, avg=avg_members, fastest_avg = fastest_avg_time)
  else:
    teams = query_service.get_teams()

    return render_template('teams.html', teams=teams, avg=avg_members, fastest_avg = fastest_avg_time)

@app.route('/members', methods=['GET', 'POST'])
@login_required
def members():
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)

  if request.method == "POST":
    teamID = request.form.get("team", "")

    if 'Member Name' in request.form.values():
      sort = 'asc'
      sort = request.form.get("member-sort", "")
      if sort == 'asc':
        members = query_service.sort_member_names_asc()
        sort = 'desc'
      else:
        members = query_service.sort_member_names_desc()
        sort = 'asc'

      return render_template('members.html', members=members, teamID=teamID, memberSort=sort)

    else:
      members = query_service.get_members_from_team(teamID)
      return render_template('members.html', members=members, teamID=teamID)

  else:
    members = query_service.get_members()
    return render_template('members.html', members=members)

@app.route('/paddles', methods=['GET', 'POST'])
@login_required
def paddles():
    conn = mysql.connection
    cur = conn.cursor()
    query_service = QueryService(cur)

    if request.method == "POST":
        memberID = request.form.get("member", "")

        if 'Manufacturer Name' in request.form.values():
            sort = 'asc'
            sort = request.form.get("paddle-sort", "")

            if sort == 'asc':
                paddles = query_service.sort_paddle_brand_asc()
                sort = 'desc'
            else:
                paddles = query_service.sort_paddle_brand_desc()
                sort = 'asc'

            return render_template('paddles.html', paddles=paddles, memberID=memberID, paddleSort=sort)
        else:
            paddles = query_service.get_paddles_from_member(memberID)
            return render_template('paddles.html', paddles=paddles, memberID=memberID)

    else:
        paddles = query_service.get_paddles()
        return render_template('paddles.html', paddles=paddles)

@app.route('/leaderboard', methods=['GET', 'POST'])
@login_required
def leaderboard():
  cur = mysql.connection.cursor()
  query_service = QueryService(cur)
  leaderboard = query_service.get_leaderboard()

  return render_template('leaderboard.html', leaderboard=leaderboard)

@app.route('/teams/<team_id>/members/<member_id>/delete', methods=['POST'])
def delete_member_path(member_id, team_id):
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)

  teamOwner =  query_service.get_user_by_team_id(team_id)

  if teamOwner == session.get('username'):
    query_service.delete_member(conn, member_id)
    flash("Member was deleted!")
    return redirect(url_for('showteam', team_id=team_id))
  else:
    flash("Cannot delete member. You are not the owner of the team")
    return redirect(url_for('showteam', team_id=team_id))

@app.route('/teams/<team_id>/delete', methods=['POST'])
@login_required
def delete_team(team_id):
    conn = mysql.connection
    cur = conn.cursor()
    query_service = QueryService(cur)

    teamOwner = query_service.get_user_by_team_id(team_id)

    if teamOwner == session.get('username'):
        query_service.move_to_freeagent(conn, team_id)
        query_service.delete_team(conn, team_id)
        flash("Team was deleted!")
        return redirect(url_for('teams'))
    else:
        flash("Cannot delete team. You are not the owner of the team")
        return redirect(url_for('teams'))

@app.route('/teams/<team_id>/members/new', methods=['GET', 'POST'])
def add_member(team_id):
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)
  form = CreateMemberForm(request.form)

  teamOwner =  query_service.get_user_by_team_id(team_id)

  if teamOwner == session.get('username'):
    if request.method == "POST":
      if form.validate() == False:
        error = "Validation failed"
        return render_template('member_new.html', form=form, error=error, team_id=team_id)
      name = form.name.data
      weight = form.weight.data
      height = form.height.data
      role = form.role.data
      paddle_side = form.paddle_side.data
      date_of_birth = form.date_of_birth.data
      last_id = query_service.get_last_member_id()
      member_id = last_id + 1
      paddle_length = height - 45

      try:

        query_service.create_member(conn, member_id, name, weight, height, role, paddle_side, date_of_birth, team_id)
        query_service.create_paddle_rental(conn, member_id, paddle_length)
        flash("Member was created!")
        return redirect(url_for('showteam', team_id=team_id))
      except Exception as e:
        flash("There was an error creating the member.")
        return redirect(url_for('add_member', team_id=team_id))
    else:
      data = query_service.get_members_from_team(0)
      return render_template('member_new.html', form=form, team_id=team_id, members=data)
  else:
    flash("Cannot add member. You are not the owner of the team")
    return redirect(url_for('showteam', team_id=team_id))


@app.route('/teams/<team_id>/members/<member_id>/update', methods=['GET', 'POST'])
def update_member(team_id, member_id):
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)
  form = UpdateMemberForm(request.form)

  if 'Update' in request.form.values():
    if form.validate() == False:
      error = "Validation failed"
      return render_template('member_update.html', form=form, team_id=team_id, member_id=member_id, error=error)
    name = form.name.data
    weight = form.weight.data
    height = form.height.data
    role = form.role.data
    paddle_side = form.paddle_side.data
    date_of_birth = form.date_of_birth.data

    try:
      query_service.update_member_by_id(conn, name, weight, height, role, paddle_side, date_of_birth, member_id)
      flash("Member was updated!")
      return redirect(url_for('showteam', team_id=team_id))
    except Exception as e:
      flash("There was an error updating the member.")
      return redirect(url_for('update_member', team_id=team_id, member_id=member_id))
  else:
    form.name.data = query_service.get_member_memberName_by_id(member_id)
    form.weight.data = query_service.get_member_weight_by_id(member_id)
    form.height.data = query_service.get_member_height_by_id(member_id)
    form.role.data = query_service.get_member_role_by_id(member_id)
    form.paddle_side.data = query_service.get_member_paddle_side_by_id(member_id)
    form.date_of_birth.data = query_service.get_member_date_of_birth_by_id(member_id)
    return render_template('member_update.html', form=form, team_id=team_id, member_id=member_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)
  try:
    form = RegistrationForm(request.form)

    if request.method == "POST" and form.validate():
      username = form.username.data
      password = form.password.data

      db_username = query_service.username_exists(username)
      hashed_password = generate_password_hash(password)

      if int(db_username) > 0:
        flash("That usename already exists!")
        return render_template("register.html", form=form)
      else:
        query_service.create_user(conn, username, hashed_password)
        flash("Thanks for registering!")
        gc.collect()

        session['logged_in'] = True
        session['username'] = username

        return redirect(url_for('dashboard'))

    return render_template("register.html", form=form)

  except Exception as e:
    return(str(e))

@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = mysql.connection
    cur = conn.cursor()
    error = None
    form = LoginForm(request.form)
    query_service = QueryService(cur)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        db_username = query_service.username_exists(username)

        if int(db_username) > 0:
          hashed_password = query_service.get_hashed_password(username)
          if check_password_hash(hashed_password, password):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
          else:
            error ='Invalid Password Credentials'
        else:
          error = 'Invalid Username Credentials'

    return render_template('login.html', form=form, error=error)

@app.route('/logout')
def logout():
  session.pop('username', None)
  session.pop('looged_in', False)
  flash("Logout succesful!")
  return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
  cur = mysql.connection.cursor()
  query_service = QueryService(cur)
  current_user = session['username']
  teams = query_service.get_current_user_teams(current_user)
  return render_template('dashboard.html', teams=teams, success=True)

@app.route('/teams/new', methods=['GET', 'POST'])
@login_required
def createteam():
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)
  form = CreateTeamForm(request.form)

  if request.method == 'POST':
    if form.validate() == False:
      error = "Validation failed"
      return render_template('new_team.html', form=form, error=error)
    team_name = form.name.data
    practice_cost = form.practice_cost.data
    city = form.city.data
    province = form.province.data
    username = session['username']

    last_id = query_service.get_last_team_id()
    team_id = last_id + 1;

    try:
      query_service.create_team(conn, team_id, team_name, practice_cost, username, city, province)
      flash("Team Created!")
    except Exception as e:
      flash("There was an error creating your team.")
      return redirect(url_for('createteam'))

    return redirect(url_for('dashboard'))

  elif request.method == 'GET':
    return render_template('new_team.html', form=form)

@app.route('/regattas/new', methods=['GET', 'POST'])
def new_regatta():
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)
  form = CreateRegattaForm(request.form)

  if request.method == 'POST':
    if form.validate() == False:
      error = "Validation Failed"
      return render_template('new_regatta.html', form=form, error=error)
    name = form.name.data
    raceLength = form.raceLength.data
    location = form.location.data
    raceDate = form.raceDate.data
    city = form.city.data
    province = form.province.data

    last_id = query_service.get_last_regatta_id()
    regatta_id = last_id + 1;

    try:
      query_service.create_regatta(conn, regatta_id, name, raceLength, location, raceDate, city, province)
      flash("Regatta Created!")
    except Exception as e:
      flash("There was an error creating your regatta.")
      return redirect(url_for('new_regatta'))

    return redirect(url_for('regattas'))

  elif request.method == 'GET':
    return render_template('new_regatta.html', form=form)

@app.route('/teams/<team_id>')
def showteam(team_id):
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)
  members = query_service.get_members_from_team(team_id)
  team = query_service.get_team_by_id(team_id)[0]
  return render_template('show_team.html', members=members, team=team)

@app.route('/members/<member_id>')
def showmember(member_id):
    conn = mysql.connection
    cur = conn.cursor()
    query_service = QueryService(cur)
    member_with_paddle = query_service.get_member_and_paddles_from_id(member_id)
    return render_template('show_member.html', members=member_with_paddle)

@app.route('/regattas/<regatta_id>')
def showraceresults(regatta_id):
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)
  raceResults = query_service.get_raceresults_join_team_from_regatta(regatta_id)
  average_time = query_service.get_average_time_from_regatta(regatta_id)[0]['AVG(timeSeconds)']
  regatta = query_service.get_regatta_by_id(regatta_id)[0]
  return render_template('raceResults.html', raceResults=raceResults, average_time=average_time, regatta=regatta)

@app.route('/chart')
def chart():
    cur = mysql.connection.cursor()
    query_service = QueryService(cur)
    leaderboard = query_service.get_leaderboard()
    numberOfTeams = query_service.get_number_of_teams_from_leaderboard()

    labels = []
    values = []
    for x in range(0, numberOfTeams):
      labels.append(leaderboard[x]['name'])
      values.append(leaderboard[x]['COUNT(resultId)'])

    return render_template('chart.html', values=values, labels=labels)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='dragonboatfelist@gmail.com', recipients=['clarencelam95@gmail.com', 'alexsclim@gmail.com'])
      msg.body = """
      From: %s
      Email: %s

      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route('/teams/<team_id>/members/<member_id>/new', methods=['POST'])
def add_free_agent(team_id, member_id):
    conn = mysql.connection
    cur = conn.cursor()
    query_service = QueryService(cur)

    query_service.move_to_team(conn, team_id, member_id)
    #flash(team_id)
    flash("member was added!")
    return redirect(url_for('showteam', team_id=team_id))
