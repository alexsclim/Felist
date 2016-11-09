from flask_wtf import Form, validators
from wtforms.fields import TextField, TextAreaField, SubmitField, PasswordField, DecimalField, SelectField
import wtforms

province_choices = [('British Columbia', 'British Columbia'), ('Ontario', 'Ontario'), ('Quebec', 'Quebec')]
city_choices = [('North Vancouver', 'North Vancouver'), ('Vancouver', 'Vancouver'), ('Chilliwack', 'Chilliwack'), ('Kelowna', 'Kelowna'),
('Harrison', 'Harrison'), ('Richmond', 'Richmond'), ('Toronto', 'Toronto'), ('Montreal', 'Montreal'), ('Victoria', 'Victoria')]

class ContactForm(Form):
  name = TextField("Name",  [wtforms.validators.Required("Please enter your name")])
  email = TextField("Email",  [wtforms.validators.Required("Please enter your email address"), wtforms.validators.Email()])
  subject = TextField("Subject",  [wtforms.validators.Required("Please enter a subject")])
  message = TextAreaField("Message",  [wtforms.validators.Required("Please enter a message")])
  submit = SubmitField("Send")

class RegistrationForm(Form):
  username = TextField('Username', [wtforms.validators.Required("Pleaser enter a username"), wtforms.validators.Length(min=4, max=20)])
  password = PasswordField('New Password', [
      wtforms.validators.Required("Please enter a password"),
      wtforms.validators.EqualTo('confirm', message='Passwords must match')
  ])
  confirm = PasswordField('Repeat Password')
  submit = SubmitField("Register")

class LoginForm(Form):
  username = TextField('Username', [wtforms.validators.Required("Please enter a username")])
  password = PasswordField('New Password', [wtforms.validators.Required("Please enter a password")])
  submit = SubmitField("Login")

class CreateTeamForm(Form):
  name = TextField('Team Name', [wtforms.validators.Required("Please enter a team name"), wtforms.validators.Length(min=1, max=50)])
  practice_cost = DecimalField('Yearly Practice Cost', [wtforms.validators.Required("Please enter a cost"), wtforms.validators.NumberRange(min=1, max=10000)])
  city = SelectField('City', [wtforms.validators.Required("Please enter a city")], choices=city_choices)
  province = SelectField('Province', [wtforms.validators.Required("Please enter a province")], choices=province_choices)
  submit = SubmitField("Create")
