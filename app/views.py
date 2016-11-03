from app import app, mail
from flask import Flask, render_template, redirect, url_for, request, flash, session, json
from functools import wraps
from forms import ContactForm, RegistrationForm
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
  db_username = cur.execute("SELECT * FROM User")
  print ('Hello')
  print db_username
  print json.dumps(cur.fetchall()[0])
  return render_template('login.html')

@app.route('/teams')
@login_required
def teams():
  return render_template('teams.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  cur = conn.cursor()
  try:
    form = RegistrationForm(request.form)

    if request.method == "POST" and form.validate():
      username = form.username.data
      password = sha256_crypt.encrypt((str(form.password.data)))

      db_username = cur.execute("SELECT * FROM User WHERE username = %s", (username))

      if int(db_username) > 0:
        flash("That usename already exists!")
        return render_template("register.html", form=form)

      else:
        cur.execute("INSERT INTO User(username, encryptedPassword) VALUES (%s, %s)", (username, password))
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
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Felix is gay. Please try again.'
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
  session.pop('username', None)
  flash("Logout succesful!")
  return redirect(url_for('login'))

@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
  return render_template('dashboard.html', success=True)

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
