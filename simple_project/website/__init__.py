# This folder is now a python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import can be written inside a function
from .views import views
from .auth import auth

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "QWBu348fD94hguth374GtbJ67384"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app