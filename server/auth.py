from flask import Blueprint, render_template, request, flash
from server.forms import SignupForm, LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
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
    signup_form = SignupForm()

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        email = signup_form.email.data
        password = signup_form.password.data
        password1 = signup_form.password1.data

        flash('Sign up successful! You can now log in.', category='success')

    else:
        # Flash first error message and stop processing
        for field, errors in signup_form.errors.items():
            flash(f"{signup_form[field].label.text}: {errors[0]}", 'error')
            break

    return render_template('signup.html', form=signup_form)

@auth.route('/logout')
def logout():
    pass
