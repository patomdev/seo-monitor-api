import logging
import pymongo
from flask import Flask, g

from . import endpoints


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)



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
     app.register_blueprint(endpoints.ping.blueprint)
     app.register_blueprint(endpoints.sitemaps.blueprint)
