from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def home():
  return render_template('index.html')
  
@app.route('/teams')
def teams():
  return render_template('teams.html')
