from app import app
from flask import Flask, render_template, redirect, url_for, request, flash
from forms import ContactForm
from flask_mail import Message
from app import mail
from table import TeamTable, TeamItem

app.secret_key = 'development key'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
  if request.method == 'POST':
    if request.form['contact'] == 'Contact Us':
      return redirect(url_for('contact'))
  return render_template('index.html')

@app.route('/teams', methods=['GET', 'POST'])
def teams():
  #items = ItemModel.query.all()
  items = [TeamItem('1', 'Dragonhearts Reborn', '220.50', '1', 'Vancouver', 'British Columbia'),
         TeamItem('2', 'Dragonhearts Thunderbreaker', '300.00', '1', 'Vancouver', 'British Columbia')]
  table = TeamTable(items)
  return render_template('teams.html', table=table)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Felix is gay. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='dragonboatfelist@gmail.com', recipients=['dragonboatfelist@gmail.com'])
      msg.body = """
      From: %s
      Email: %s

      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)
