from flask import Flask
from flaskext.mysql import MySQL
from flask_mail import Message, Mail

from forms import ContactForm
from flask import render_template, request

mail = Mail()
mysql = MySQL()
app = Flask(__name__)
from app import views

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dragonboatfelist@gmail.com'
app.config['MAIL_PASSWORD'] = 'felist123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'Felist'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

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
