#!/usr/bin/python3
""" the Script to start a Flask web application with 2 commands """

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Return other text. """
    return 'HBNB'

if __name__ == '__main__':
    #This starts the flask devp server
    #This listens on all available network interface (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)
