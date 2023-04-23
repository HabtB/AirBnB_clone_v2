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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    " returns for the '/hbnb' route/"
    if isinstance(n, int):
        return render_template('5-number_template.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n=None):
    if (type(n) == int):
        EorO = "even" if (n % 2 == 0) else "odd"
        return render_template('6-number_odd_or_even.html', n=n, EorO=EorO)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
