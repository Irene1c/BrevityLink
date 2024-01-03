"""auth views"""
from flask import Blueprint, render_template, flash, redirect, url_for
from server.forms import SignupForm, LoginForm
from server.models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """login view"""

    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('app_views.home'))
            else:
                flash('Incorrect password! Try again', category='error')
        else:
            flash('Email Address does not exist!', category='error')
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

        login_user(new_user, remember=True)
        flash('Account created! You are now logged in.', category='success')
        return redirect(url_for('app_views.home'))

    else:
        # Flash first error message and stop processing
        for field, errors in signup_form.errors.items():
            flash(f"{signup_form[field].label.text}: {errors[0]}", 'error')
            break

    return render_template('signup.html', form=signup_form)


@auth.route('/logout')
@login_required
def logout():
    """logout a user"""

    logout_user()
    return redirect('/login')
