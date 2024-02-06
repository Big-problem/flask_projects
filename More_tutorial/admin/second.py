from flask import Blueprint, render_template

# This variable is what imported in the main.py
second = Blueprint("second", __name__, static_folder="static", static_url_path="", template_folder="templates")

@second.route("/home")
@second.route("/")
def index():
    return render_template("index.html")

@second.route("test")
def test():
    return "<h1>Blueprint Test</h1>"