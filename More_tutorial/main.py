from flask import Flask, render_template
from admin.second import second

app = Flask(__name__)
# Use the blieprint when the url is /admin...
app.register_blueprint(second, url_prefix="/admin")

@app.route("/") # Can have multiple routes
@app.route("/home")
def index():
    return "<h1>Test</h1>"

if __name__ == "__main__":
    app.run(debug=True)