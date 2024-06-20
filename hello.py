from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello Python</h1>"


# @app.route("/japan/<city>")
# def tokyo(city):
#     return f'Hello, { city } in Japan'

# @app.route("/japan/tokyo")
# def tokyo():
#     return "Hello,tokyo in Japan"

# @app.route("/japan/ohsaka")
# def ohsaka():
#     return "Hello,ohsaka in Japan"

# @app.route("/japan/kyoto")
# def kyoto():
#     return "Hello,kyoto in Japan"


# @app.route("/baseball/ohtani")
# def baseball():
#     return "Ohtani"

# @app.route("/football/messi")
# def football():
#     return "Messi"

