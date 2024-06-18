from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World"

@app.route("/baseball")
def baseball():
    return "Ohtani"

@app.route("/football")
def football():
    return "Messi"

