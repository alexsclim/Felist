from app import app
from flask import Flask, render_template, redirect, url_for, request

@app.route('/')
@app.route('/index')
def home():
  return render_template('index.html')

@app.route('/teams')
def teams():
  return render_template('teams.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Felix is gay. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
