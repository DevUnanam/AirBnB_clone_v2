#!/usr/bin/python3
<<<<<<< HEAD
""" This adds fifth view func that displays HTML page if n is int """

from flask import Flask
from flask import render_template


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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """ replace more text with another variable. """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_text(n):
    """ replace with int only if given int. """
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def html_num(n):
    """ display html if n is int. """
    n = str(n)
=======
"""Flask module"""

from flask import Flask, render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def textpython(text='is cool'):
    """Displays 'Python' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "Python {}".format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """displays “<n> is a number” only if n is an integer"""
    return "{} is a number".format(escape(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays “<n> is a number” only if n is an integer"""
>>>>>>> 80456ae28d0d42f19febaaa767fdff2de4cd8244
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
    app.run(host='0.0.0.0')
>>>>>>> 80456ae28d0d42f19febaaa767fdff2de4cd8244
