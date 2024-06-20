from flask import Flask

app = Flask(__name__)

html = '''
<h1>HTMLの練習</h1>
<ul>
    <li>リスト1</li>
    <li>リスト2</li>
    <li>リスト3</li>
</ul>

'''

@app.route("/")
def hello():
    return html


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

