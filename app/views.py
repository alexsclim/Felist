from app import app, mail
from flask import Flask, render_template, redirect, url_for, request, flash, session, json
from functools import wraps
from forms import ContactForm, RegistrationForm, LoginForm, CreateTeamForm
from flask_mail import Message
from passlib.hash import sha256_crypt

import gc

from app import mysql

app.secret_key = 'development key'

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
  last_id = cur.execute("SELECT * From Team")
  print session
  print last_id
  return render_template('dashboard.html')

@app.route('/teams')
@login_required
def teams():
  cur = mysql.connection.cursor()
  cur.execute("SELECT * from Team")

  rows = cur.fetchall();
  return render_template('teams.html', rows=rows)

@app.route('/register', methods=['GET', 'POST'])
def register():
  conn = mysql.connection
  cur = conn.cursor()
  try:
    form = RegistrationForm(request.form)

    if request.method == "POST" and form.validate():
      username = form.username.data
      password = form.password.data

      db_username = cur.execute("SELECT * FROM User WHERE username = %s", [username])

      if int(db_username) > 0:
        flash("That usename already exists!")
        return render_template("register.html", form=form)

      else:
        cur.execute("INSERT INTO User(username, encryptedPassword) VALUES (%s, %s)", [username, password])
        conn.commit()
        flash("Thanks for registering!")
        gc.collect()

        session['logged_in'] = True
        session['username'] = username

        return redirect(url_for('dashboard'))

    return render_template("register.html", form=form)

  except Exception as e:
    return(str(e))

@app.route('/', methods=['GET'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = mysql.connection
    cur = conn.cursor()
    error = None

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        db_username = cur.execute("SELECT * FROM User WHERE username= %s", [username])
        db_password = cur.execute("SELECT * FROM User WHERE username= %s and encryptedpassword=%s", [username, password])
        if int(db_username) > 0:
          if int(db_password) > 0:
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
  flash("Logout succesful!")
  return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
  conn = mysql.connection
  cur = conn.cursor()
  current_user = session['username']
  cur.execute("SELECT name FROM Team WHERE username= %s", [current_user])

  teams = cur.fetchall()
  print teams[0]
  return render_template('dashboard.html', teams=teams, success=True)

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

@app.route('/teams/new', methods=['GET', 'POST'])
@login_required
def createteam():
  conn = mysql.connection
  cur = conn.cursor()
  form = CreateTeamForm(request.form)

  if request.method == 'POST' and form.validate():
    team_name = form.name.data
    practice_cost = form.practice_cost.data
    city = form.city.data
    province = form.province.data
    username = session['username']

    last_id = cur.execute("SELECT * From Team")
    team_id = last_id + 1;

    cur.execute("INSERT INTO Team(teamId, name, practiceCost, username, regionCity, regionProvince) VALUES (%s, %s, %s, %s, %s, %s)", [team_id, team_name, practice_cost, username, city, province])
    conn.commit()
    flash("Team Created!")

    return redirect(url_for('dashboard'))

  elif request.method == 'GET':
    return render_template('new_team.html', form=form)
