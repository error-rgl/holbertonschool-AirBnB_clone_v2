#!/usr/bin/python3
""" Module that start a Flask Webb app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Route /c"""
    return "C %s" % text.replace("_", " ")


if __name__ == '__main__':
    """application must be listening on"""
    app.run(host='0.0.0.0', port='5000')
