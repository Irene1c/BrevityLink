"""auth views"""
from flask import Blueprint, render_template, flash, redirect, url_for
from server.forms import SignupForm, LoginForm
from server.models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """login view"""

    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        flash('Logged in.', category='success')
    else:
        for field, errors in login_form.errors.items():
            flash(f"{login_form[field].label.text}: {errors[0]}", 'error')
            break

    return render_template('login.html', form=login_form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """signup view"""

    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        email = signup_form.email.data
        password = signup_form.password.data
        password1 = signup_form.password1.data

        new_user = User(
                username=username, email=email,
                password=generate_password_hash(
                    password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()

        flash('Account created! You are now logged in.', category='success')
        return redirect(url_for('app_views.home'))

    else:
        # Flash first error message and stop processing
        for field, errors in signup_form.errors.items():
            flash(f"{signup_form[field].label.text}: {errors[0]}", 'error')
            break

    return render_template('signup.html', form=signup_form)


@auth.route('/logout')
def logout():
    """logout"""

    pass
