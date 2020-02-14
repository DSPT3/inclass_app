from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!!!! Welcome to Flask!"

@app.route("/about")
def about():
    return "About Me!"


