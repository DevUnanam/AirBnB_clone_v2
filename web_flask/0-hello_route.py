#!/usr/bin/python3
<<<<<<< HEAD
""" The Script to start a Flask web application """

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
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
=======
def hello():
    """Greetings, hbnb project"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
>>>>>>> 80456ae28d0d42f19febaaa767fdff2de4cd8244
