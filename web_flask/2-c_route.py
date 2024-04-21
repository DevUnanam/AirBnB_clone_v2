#!/usr/bin/python3
<<<<<<< HEAD
""" The Script to start a Flask web application with 3 view functions """

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """ Return other text. """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """ replace text with variable. """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)
=======
"""starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Greetings, hbnb project"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_c(text):
    """Displays 'C' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C {}".format(escape(text))
>>>>>>> 80456ae28d0d42f19febaaa767fdff2de4cd8244


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
