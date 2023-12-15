from flask import Flask
from server.views import app_views
from server.auth import auth

def create_app():
    """application factory"""

    app = Flask(__name__)

    # load configuration settings
    app.config.from_object('config.ConfigClass')

    app.register_blueprint(app_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
