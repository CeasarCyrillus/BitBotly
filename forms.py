from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from flask_login import login_user, logout_user, current_user, login_required
from wtforms.widgets import TextArea
from models import User
from sqlalchemy import *
from validators import v


class Signup_form(Form):
    username = StringField("Username", validators=v["signup"]["username"])
    email = StringField('Email')
    password = PasswordField('Password', validators=v["signup"]["password"])
    first_name = StringField("First name")
    last_name = StringField("Last name")
    submit = SubmitField("Sign up")
        
        
class Login_form(Form):
    username = StringField('Username', validators=v["login"]["username"])
    password = PasswordField('Password', validators=v["login"]["password"])
    submit = SubmitField("Login")

class Post_form(Form):
    main_image = StringField("Image", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", widget=TextArea(), validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    submit = SubmitField("Add post")

class Contact_form(Form):
    email = StringField("Email", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")