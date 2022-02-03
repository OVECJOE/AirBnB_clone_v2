#!/usr/bin/python3
"""A script that starts a Flask web application"""
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


@app.route('/python', strict_slashes=False, defaults={'text': "is_cool"})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python " + " ".join(text.split("_"))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return """<!DOCTYPE html>
<HTML lang="en">
  <HEAD>
      <TITLE>HBNB</TITLE>
  </HEAD>
  <BODY>
      <H1>Number: {}</H1>
  </BODY>
</HTML>""".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
