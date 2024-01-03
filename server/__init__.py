"""flask app"""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """application factory"""

    app = Flask(__name__)

    # load configuration settings
    app.config.from_object('config.ConfigClass')

    # Enable CSRF protection globally
    csrf = CSRFProtect(app)

    # setup the database
    db.init_app(app)

    from server.views import app_views
    from server.auth import auth

    app.register_blueprint(app_views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # loading models to create the database
    from server.models import User, Url

    # create the database
    with app.app_context():
        db.create_all()
        print('Database created')

    # view when user is not logged in
    login_manager.login_view = 'auth.login'

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        """User loading function"""

        return User.query.get(id)

    return app
