#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_framework():
    """ display Hello HBNB! """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """application must be listening on"""
    app.run(host='0.0.0.0', port='5000')
    app.url_map.strict_slashes = False
