from flask import Flask

app = Flask(__name__)

@app.route("/")
# route decorators are used to add additional functionalities
def hello_world():
    return "<p>Hello, World!</p>"
