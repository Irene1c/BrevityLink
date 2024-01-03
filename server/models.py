"""Database models"""
from . import db
from datetime import datetime
from flask_login import UserMixin
import random
import string
import uuid


class User(db.Model, UserMixin):
    """ class to define each user"""

    id = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()))
    username = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    urls = db.relationship('Url')


class Url(db.Model):
    """ class to define users urls """

    id = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()))
    long_url = db.Column(db.String(500))
    short_url = db.Column(db.String(20), unique=True)
    clicks = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        """class constructor"""

        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self):
        """Method to generate short url"""

        chars = string.ascii_letters + string.digits
        short_url = ''.join(random.choices(chars, k=6))

        url = self.query.filter_by(short_url=short_url).first()

        if url:
            return self.generate_short_url()

        return short_url
