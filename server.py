import os
from core.factories import create_app, SettingsError

if __name__ == '__main__':
    if os.environ['APP_SETTINGS']:
        settings_name = os.environ['APP_SETTINGS']
    else:
        raise SettingsError("\'APP_SETTINGS\' environment "
                            "variable is not defined")
    app = create_app(__name__, settings_name)
    app.run(debug=app.app.config['DEBUG'], host='0.0.0.0', port=80)
