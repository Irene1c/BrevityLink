"""app forms"""
from flask_wtf import FlaskForm
from server.models import User
from wtforms import StringField, PasswordField, SubmitField, validators


class SignupForm(FlaskForm):
    """Defining the signup form"""

    username = StringField('Username', validators=[validators.Length(min=2)])
    email = StringField('Email Address', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=6)])
    password1 = PasswordField(
            'Confirm Password', validators=[validators.EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        """check if an email already exists"""

        existing_email = User.query.filter_by(email=email.data).first()
        if existing_email:
            raise validators.ValidationError('Email Address already exists!')


class LoginForm(FlaskForm):
    """Defining the login form"""

    email = StringField('Email Address', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=6)])
    submit = SubmitField('Login')


class ShortenURLForm(FlaskForm):
    """Defining the url form"""

    long_url = StringField('URL', validators=[validators.URL()])
    submit = SubmitField('Shorten URL')
