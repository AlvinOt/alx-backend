#!/usr/bin/env python3
"""A Flask app
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Flask app config

    Class defining config options for the Flask app.

    Attributes:
        LANGUAGES (list): List of available languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for Babel.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Configure the Flask app


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get best-matching locale based on client's preferred languages.

    Returns:
        str: The best-matching locale from the supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the index page.

    Returns:
        str: Rendered HTML content.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
