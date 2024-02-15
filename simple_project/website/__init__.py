# This folder is now a python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "QWBu348fD94hguth374GtbJ67384"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # import .models as models
    from .models import Note, User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # "get" will look for primary key automatically
        return User.query.get(int(id))

    return app

def create_database(app):
    """
        Check if the database exists
    """
    # Be aware of the path
    if not path.exists("./simple_project/instance/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("### Created Database! ###")