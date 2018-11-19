from wtforms.validators import DataRequired, Email, Length, Regexp, ValidationError
from models import User
def username_must_not_exists(message):
    def _username_must_not_exists(form, field):
        if field.data and len(field.data):
            user = User.query.filter_by(username=field.data).first()
            if user:
                raise ValidationError(message)
        else:
            raise ValidationError(message)
        return True
    return _username_must_not_exists

def email_must_not_exists(message):
    def _email_must_not_exists(form, field):
        if field.data and len(field.data):
            user = User.query.filter_by(email=field.data).first()
            if user:
                raise ValidationError(message)
        else:
            raise ValidationError(message)
        return True
    return _email_must_not_exists

def username_must_exists(message):
    def _username_must_exists(form, field):
        if field.data and len(field.data):
            user = User.query.filter_by(username=field.data).first()
            if not user:
                raise ValidationError(message)
        else:
            raise ValidationError(message)
        return True
    return _username_must_exists

def email_must_exists(message):
    def _email_must_exists(form, field):
        if field.data and len(field.data):
            user = User.query.filter_by(email=field.data).first()
            if not user:
                raise ValidationError(message)
        else:
            raise ValidationError(message)
        return True
    return _email_must_exists

v = {
    "signup": {
        "username": [
            Length(min=3, message="username must be atleast 3 characters long"),
            Length(max=30, message="username must be atmost 30 characters long"),
            Regexp('[A-Za-z0-9_-]', message="username can only contain letters, numbers and underscore"),
            username_must_not_exists(message="username is already in use")
        ],

        "password": [
            Length(min=6, message="password must be atleast 6 characters long"),
            Length(max=256, message="password must be atmost 256 characters long"),
        ]
    },

    "login": {
        "username": [
            Length(min=1, message="please enter your username"),
            username_must_exists(message="no user found with that username")
        ],

        "email": [
            Email(message="email must be a valid email")
        ],

        "password": [
            Length(min=1, message="please enter your password"),
        ]
    },

    "contact": {
        "email": [
            Email()
        ]
    }
}