import logging
from urllib.parse import unquote
from flask import url_for, current_app

log = logging.getLogger(__name__)


def route(*args, **kwargs):
    """Unquoted version of Flask's `url_for`."""
    return _secure(unquote(url_for(*args, **kwargs)))


def _secure(url):
    """Ensure HTTPS is used in production."""
    if current_app.config['ENV'] == 'prod':
        url = url.replace('http:', 'https:')
    return url


def _nocache(response):
    """Ensure a response is not cached."""
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
