from app import app
from flask import Flask, render_template, redirect, url_for, request, flash
from table import TeamTable, TeamItem
# from forms import ContactForm
# from flask_mail import Message

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
