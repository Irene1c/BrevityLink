from flask import Blueprint, render_template, request, flash
from server.form import SignupForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password1 = form.password1.data

        flash('Sign up successful! You can now log in.', category='success')

    else:
        # Flash first error message and stop processing
        for field, errors in form.errors.items():
            flash(f"{form[field].label.text}: {errors[0]}", 'error')
            break

    return render_template('signup.html', form=form)

@auth.route('/logout')
def logout():
    pass
