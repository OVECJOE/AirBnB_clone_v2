#!/usr/bin/python3
"""A script that starts a web application"""
from re import L
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C " + " ".join(text.split("_"))


@app.route('/python', defaults={'text': "is_cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python " + " ".join(text.split("_"))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
