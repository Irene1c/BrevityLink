from flask import Blueprint, render_template, flash
from server.forms import ShortenURLForm

app_views = Blueprint('app_views', __name__)

@app_views.route('/', methods=['GET', 'POST'])
def home():
    url_form = ShortenURLForm()

    if url_form.validate_on_submit():
        long_url = url_form.long_url.data
    else:
        for field, errors in url_form.errors.items():
            flash(f"{url_form[field].label.text}: {errors[0]}", 'error')
            break
    return render_template('home.html', form=url_form)
