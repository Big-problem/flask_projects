from flask import Flask, redirect, url_for

# Create instance of flask app
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello! This is the index page <h1>HELLO</h1>"

@app.route("/<name>") # Pass the parameter inside <> to the function
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin(): # Redirect the page tp the function instde ""
    return redirect(url_for("index"))


# Run the app
if __name__ == "__main__":
    app.run()