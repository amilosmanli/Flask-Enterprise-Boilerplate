import os

from flask_script import Manager

from core.factories import create_app

config_name = os.getenv('APP_SETTINGS', 'default')
app = create_app(__name__, config_name)

manager = Manager(app)


if __name__ == "__main__":
    manager.run()
