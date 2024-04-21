#!/usr/bin/python3
<<<<<<< HEAD
""" the Script to start a Flask web application with 2 commands """

from flask import Flask


=======
"""Flask module"""

from flask import Flask

>>>>>>> 80456ae28d0d42f19febaaa767fdff2de4cd8244
app = Flask(__name__)


@app.route('/', strict_slashes=False)
<<<<<<< HEAD
def hello_world():
    """ Returns some text. """
=======
def hello():
    """Greetings, hbnb project"""
>>>>>>> 80456ae28d0d42f19febaaa767fdff2de4cd8244
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
<<<<<<< HEAD
def hello():
    """ Return other text. """
    return 'HBNB'

if __name__ == '__main__':
    #This starts the flask devp server
    #This listens on all available network interface (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
=======
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> 80456ae28d0d42f19febaaa767fdff2de4cd8244
