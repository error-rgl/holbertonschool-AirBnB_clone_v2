#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_route():
    """renders 7-states_list.html"""
    states = storage.all(State)
    new_dic = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           items=new_dic)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
