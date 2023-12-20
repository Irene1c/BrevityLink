from flask import Flask
from server.views import app_views
from server.auth import auth
from flask_wtf.csrf import CSRFProtect



def create_app():
    """application factory"""

    app = Flask(__name__)

    # load configuration settings
    app.config.from_object('config.ConfigClass')

    # Enable CSRF protection globally
    csrf = CSRFProtect(app)

    app.register_blueprint(app_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
