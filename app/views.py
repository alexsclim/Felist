from app import app, mail, mysql
from flask import Flask, render_template, redirect, url_for, request, flash, session, json
from forms import ContactForm, RegistrationForm, LoginForm, CreateTeamForm
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

  if request.method == "POST":
    if 'Search Regattas' in request.form.values():
      search = request.form['search-input']
      regattas = query_service.search_regattas(search)

      return render_template('regattas.html', regattas=regattas)

  else:
    regattas = query_service.get_regattas()

    return render_template('regattas.html', regattas=regattas)

@app.route('/teams', methods=['GET', 'POST'])
@login_required
def teams():

  cur = mysql.connection.cursor()
  query_service = QueryService(cur)

  if request.method == "POST":
    if 'Search Team' in request.form.values():
      search = request.form['search-input']
      teams = query_service.search_teams(search)

      return render_template('teams.html', teams=teams)

    else:
      team_id = request.form['team']

      members = query_service.get_members_from_team(team_id)
      return render_template('members.html', members=members, memberDelete=memberDelete)

  else:
    teams = query_service.get_teams()

    return render_template('teams.html', teams=teams)

@app.route('/members', methods=['GET', 'POST'])
@login_required
def members():
  conn = mysql.connection
  cur = conn.cursor()
  query_service = QueryService(cur)

  if request.method == "POST":
    teamID = request.form.get("team", "")

    if 'Delete' in request.form.values():
      memberDelete = 'true'

      memberId = request.form.get("member-id", "")
      query_service.delete_member(conn, memberId)

      members = query_service.get_members_from_team(teamID)

      return render_template('members.html', members=members, memberDelete=memberDelete, teamID=teamID)


    if 'Member Name' in request.form.values():
      if request.form.get("member-delete", "") == 'true':
        sort = 'asc'
        sort = request.form.get("member-sort", "")
        if sort == 'asc':
          members = query_service.sort_member_names_by_team_asc(teamID)
          sort = 'desc'
        else:
          members = query_service.sort_member_names_by_team_desc(teamID)
          sort = 'asc'

        memberDelete = 'true'
        return render_template('members.html', members=members, teamID=teamID, memberDelete=memberDelete, memberSort=sort)

      else:
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
      memberDelete = 'true'

      members = query_service.get_members_from_team(teamID)
      return render_template('members.html', members=members, memberDelete=memberDelete, teamID=teamID)

  else:
    memberDelete = None
    members = query_service.get_members()
    return render_template('members.html', members=members, memberDelete=memberDelete)

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

  if request.method == 'POST' and form.validate():
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

@app.route('/teams/<int:team_id>')
def showteam():
  return render_template('show_team.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='dragonboatfelist@gmail.com', recipients=['clarencelam95@gmail.com'])
      msg.body = """
      From: %s
      Email: %s

      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)
