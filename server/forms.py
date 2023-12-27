"""app forms"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class SignupForm(FlaskForm):
    """Defining the signup form"""

    username = StringField('Username', validators=[validators.Length(min=2)])
    email = StringField('Email', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=6)])
    password1 = PasswordField(
            'Confirm Password', validators=[validators.EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    """Defining the login form"""

    email = StringField('Email', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=6)])
    submit = SubmitField('Login')


class ShortenURLForm(FlaskForm):
    """Defining the url form"""

    long_url = StringField('URL', validators=[validators.URL()])
    submit = SubmitField('Shorten URL')
