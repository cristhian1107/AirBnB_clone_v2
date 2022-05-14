#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def path():
    """
    Function that display text on screen - web route (/).
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def path_hbnb():
    """
    Function that display text on screen - web route (/hbnb).
    """
    return 'HBNB'


@app.route('/c/<custom>', strict_slashes=False)
def path_c_custom(custom):
    """
    Function that display custom text on screen - web route custom (/c/<custom>).
    """
    return 'C %s' % custom.replace('_', ' ')


@app.route('/python', defaults={'custom': 'is cool'}, strict_slashes=False)
@app.route('/python/<path:custom>', strict_slashes=False)
def path_python_custom(custom):
    """
    Function that display custom text on screen - web route custom (/c/<text>).
    """
    return "Python {}".format(custom.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
