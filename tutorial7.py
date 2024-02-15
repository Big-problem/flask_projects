from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "HeLLo" # Session needs a secret key
app.permanent_session_lifetime = timedelta(minutes=5)

# Setup for database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create database
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email  = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route("/")
def index():
    return render_template("extend.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # Make this a permanent session
        # key is the value of name
        user = request.form["nm"]
        # Using session
        session["user"] = user

        # query the database
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else: # Create new user in the database
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login successfully")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
     
        return render_template("login.html") 
    
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            ### The line below can get multiple results
            # found_user = users.query.filter_by(name=user).first()
            ### Use .delete to delete something in the database
            # for user in found_user:
            #       user.delete()   // Remember to commit() in the end
            found_user.email = email
            db.session.commit()
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", user=user, email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout(): # Delete session
    if "user" in session:
        user = session["user"]
        session.pop("user", None)
        session.pop("email", None)
        # Flash messages
        flash(f"{user} logout successfully", "info")
    return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Create the database if it doesn't exist
        print("XXXZZZYYY")
    app.run(debug=True)