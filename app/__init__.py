import sys

__project__ = 'seomonitor'
__version__ = 'v1'
VERSION = "{} v{}".format(__project__, __version__)

PYTHON_VERSION = 3, 5

if sys.version_info < PYTHON_VERSION:  # pragma: no cover (manual test)
    exit("Python {}.{}+ is required.".format(*PYTHON_VERSION))

import logging
from flask import Flask
from config import config
from . import endpoints


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    configure_logging(app)
    register_endpoints(app)

    return app

def configure_logging(app):
    if app.config['DEBUG']:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")
    logging.getLogger('yorm').setLevel(logging.WARNING)
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('PIL').setLevel(logging.INFO)

def register_endpoints(app):
    app.register_blueprint(endpoints.root.blueprint)
    app.register_blueprint(endpoints.pages.blueprint)
