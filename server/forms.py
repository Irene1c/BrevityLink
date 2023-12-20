from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask import flash

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[validators.Length(min=2)])
    email = StringField('Email', validators=[validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(min=6)])
    password1 = PasswordField('Confirm Password', validators=[validators.EqualTo('password')])
    submit = SubmitField('Sign Up')
