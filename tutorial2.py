from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(): # Render HTML file inside a folder named templates (name of the folder cannot change)
    # inside html, we can use {{}} to pass parameters
    # Add the parameter after the html file name
    # Use {%%} to write some python code in html file
    return render_template("index.html", name="Home")

@app.route("/<name>")
def user(name):
    l = ["Ted", "Joe", "Jack"]
    return render_template("index.html", name=name, content=l)

if __name__ == "__main__":
    app.run()