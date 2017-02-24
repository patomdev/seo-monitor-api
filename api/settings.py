import os

class Config:
    """Basic configuration"""
    ENV = None

    PATH = os.path.abspath(os.path.dirname(__file__))
    ROOT = os.path.dirname(PATH)
    DEBUG = False
    THREADED = False

    """Mongo configuration"""
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'localhost')
    MONGODB_PORT = os.getenv('MONGODB_PORT', 27017)
    MONGODB_DB = os.getenv('MONGODB_DB', 'your_db')


class ProdConfig(Config):
    """Production configuration"""

    ENV = 'prod'


class TestConfig(Config):
    """Test configuration."""

    ENV = 'test'

    DEBUG = True
    TESTING = True


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'

    DEBUG = True

def get_config(name):
    assert name, "No configuration specified"

    for config in Config.__subclasses__():
        if config.ENV == name:
            return config

    assert False, "No matching configuration: {}".format(name)

