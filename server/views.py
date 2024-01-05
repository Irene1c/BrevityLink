"""app views"""
from flask import Blueprint, render_template, flash, redirect, url_for, abort
from server.forms import ShortenURLForm
from server.models import Url
from . import db
from flask_login import current_user, login_required


app_views = Blueprint('app_views', __name__)


@app_views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """home view"""

    url_form = ShortenURLForm()

    if url_form.validate_on_submit():
        long_url = url_form.long_url.data

        existing_url = Url.query.filter_by(
                long_url=long_url, user_id=current_user.id).first()
        if existing_url:
            flash('URL has already been shortened!', category='error')
        else:
            # associate the url with current user
            new_url = Url(long_url=long_url, user_id=current_user.id)
            db.session.add(new_url)
            db.session.commit()

            flash('URL shortened successfully', 'success')

        form_submitted = True

        # redirect page after form submission
        return redirect(url_for('app_views.home'))

    else:
        for field, errors in url_form.errors.items():
            flash(f"{url_form[field].label.text}: {errors[0]}", 'error')
            break

        form_submitted = False

    # Use the 'urls' relationship to get a user's URLs
    user_urls = current_user.urls

    return render_template(
            'home.html',
            form=url_form, user_urls=user_urls, form_submitted=form_submitted)


@app_views.route('/<short_url>')
@login_required
def redirect_url(short_url):
    """redirect the short url to its corresponding long url"""

    url = Url.query.filter_by(short_url=short_url).first()
    if url:
        # increment click count
        url.clicks = url.clicks + 1
        db.session.commit()

        # redirecting to long url
        return redirect(url.long_url)
    else:
        abort(404)


@app_views.route('/delete_url/<url_id>', methods=['POST'])
@login_required
def delete_url(url_id):
    """deletes a url"""

    url = Url.query.get(url_id)

    if url and url.user_id == current_user.id:
        db.session.delete(url)
        db.session.commit()
        flash('URL deleted successfully', 'success')

    #reload the page to update the url table
    return redirect(url_for('app_views.home'))
