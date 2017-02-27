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

    SWAGGER_UI_URI = "http://localhost:8080"

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

config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig,
    'default': DevConfig
}
