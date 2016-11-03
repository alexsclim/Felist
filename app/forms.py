from flask_wtf   import Form, validators
from wtforms.fields import TextField, TextAreaField, SubmitField, PasswordField, DecimalField
import wtforms

class ContactForm(Form):
  name = TextField("Name",  [wtforms.validators.Required("Please enter your name")])
  email = TextField("Email",  [wtforms.validators.Required("Please enter your email address"), wtforms.validators.Email()])
  subject = TextField("Subject",  [wtforms.validators.Required("Please enter a subject")])
  message = TextAreaField("Message",  [wtforms.validators.Required("Please enter a message")])
  submit = SubmitField("Send")

class RegistrationForm(Form):
  username = TextField('Username', [wtforms.validators.Length(min=4, max=20)])
  password = PasswordField('New Password', [
      wtforms.validators.Required(),
      wtforms.validators.EqualTo('confirm', message='Passwords must match')
  ])
  confirm = PasswordField('Repeat Password')
  submit = SubmitField("Register")

class LoginForm(Form):
  username = TextField('Username')
  password = PasswordField('New Password')
  submit = SubmitField("Login")

class CreateTeamForm(Form):
  name = TextField('Team Name', [wtforms.validators.Length(min=1, max=50)])
  practice_cost = DecimalField('Yearly Practice Cost')
  city = TextField('City', [wtforms.validators.Length(min=1)])
  province = TextField('Province', [wtforms.validators.Length(min=1)])
  submit = SubmitField("Create")
