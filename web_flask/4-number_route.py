#!/usr/bin/python3
""" A script that starts a Flask Application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns for the '/' route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns for the '/hbnb' route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_text(text):
    """ returns for the '/c/<text>' route"""
    return "C {}".format(text.replace('_', " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text="is cool"):
    """ returns for the '/python/<text>' route"""
    return "Python {}".format(text.replace('_', " "))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    " returns for the '/hbnb' route/"
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
