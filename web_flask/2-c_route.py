#!/usr/bin/python3
""" A script that starts a Flask Application"""
from flask import Flask, render_template
import re
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
    new_text = re.sub('_', " ", text)
    return f"C {new_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
