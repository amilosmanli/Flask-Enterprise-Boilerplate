import os
import os.path as op

from connexion import FlaskApp
from flask_script import Manager

from core.extensions import db, ma


settings = {
    'development': 'core.settings.DevelopmentConfig',
    'production': 'core.settings.ProductionConfig',
    'testing': 'core.settings.TestingConfig',
    'default': 'core.settings.DevelopmentConfig'
}


class SettingsError(Exception):
    def __init__(self, setting_name):
        super(Exception, self)\
            .__init__("Given application setting does not exist: %s"
                      % setting_name)
        self.setting_name = setting_name


class SwaggerError(Exception):
    def __init__(self, message):
        super(Exception, self).__init__(message)


def get_config(setting_name):
    if settings.get(setting_name):
        return settings.get(setting_name)
    else:
        raise SettingsError(setting_name)


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    return None


def register_api(app):
    swagger_path = op.abspath(op.join(op.dirname(__name__), 'swagger'))
    if op.exists(swagger_path):
        for api in os.listdir(swagger_path):
            app.add_api(op.join(swagger_path, api))
    else:
        raise SwaggerError("Folder containing swagger files doesn't exists in "
                           "current directory.")
    return None


def create_app(app_name, config_name):
    config_obj = get_config(config_name)

    cnnx_app = FlaskApp(app_name)
    flask_app = cnnx_app.app
    flask_app.app_context().push()
    flask_app.config.from_object(config_obj)

    register_extensions(flask_app)
    register_api(cnnx_app)

    return flask_app


def get_manager(app_name, config_name):
    app = create_app(app_name, config_name)
    return Manager(app)
