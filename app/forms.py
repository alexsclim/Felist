from flask.ext.wtf import Form, validators
from wtforms.fields import TextField, TextAreaField, SubmitField
import wtforms

class ContactForm(Form):
  name = TextField("Name",  [wtforms.validators.Required("Please enter your name")])
  email = TextField("Email",  [wtforms.validators.Required("Please enter your email address"), wtforms.validators.Email()])
  subject = TextField("Subject",  [wtforms.validators.Required("Please enter a subject")])
  message = TextAreaField("Message",  [wtforms.validators.Required("Please enter a message")])
  submit = SubmitField("Send")
