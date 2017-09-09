import os

from core.factories import get_manager

config_name = os.getenv('APP_SETTINGS', 'default')
manager = get_manager(__name__, config_name)


if __name__ == "__main__":
    manager.run()
