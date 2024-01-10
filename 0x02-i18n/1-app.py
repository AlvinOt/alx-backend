#!/usr/bin/env python3
"""This is a flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """Flask app config

    A class defining configuration options for Flask app.

    Attributes:
        LANGUAGES (list): List of available lang.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Configure the Flask app


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Render index page

    Function renders index.html template.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
