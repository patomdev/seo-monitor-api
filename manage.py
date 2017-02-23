import os
from flask_script import Command, Manager, Server

from api.settings import get_config
from api.app import create_app

config = get_config(os.getenv('FLASK_CONFIG', 'dev'))

app = create_app(config)

manager = Manager(app)
manager.add_command('run', Server(host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()
