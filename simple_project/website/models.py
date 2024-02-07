from . import db # db is in __init__.py
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone=True), default=func.now)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True) # Email needs to be unique
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))