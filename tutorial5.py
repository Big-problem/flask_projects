from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "HeLLo"
app.permanent_session_lifetime = timedelta(minutes=5)

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
        flash("Login successfully")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in")
            return redirect(url_for("user"))
     
        return render_template("login.html") 
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout(): # Delete session
    if "user" in session:
        user = session["user"]
        session.pop("user", None)
        # Flash messages
        flash(f"{user} logout successfully", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)