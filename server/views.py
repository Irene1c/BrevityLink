
from flask import Blueprint, render_template

app_views = Blueprint('app_views', __name__)

@app_views.route('/')
def home():
    return render_template('home.html')
