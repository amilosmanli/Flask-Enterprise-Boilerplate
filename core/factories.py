import sys
import os
import os.path as op
import logging

from connexion import FlaskApp

from core.extensions import db, ma


settings = {
    'development': 'core.settings.DevelopmentConfig',
    'production': 'core.settings.ProductionConfig',
    'testing': 'core.settings.TestingConfig',
    'default': 'core.settings.DevelopmentConfig'
}


class SettingsError(Exception):
    pass


class SwaggerError(Exception):
    pass


def get_config(setting_name):
    if settings.get(setting_name):
        return settings.get(setting_name)
    else:
        raise SettingsError("Given settings name does not exists: %s"
                            % setting_name)


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
    flask_app.config.from_object(config_obj)
    flask_app.app_context().push()

    log_formatter = logging.Formatter(
        "[%(asctime)s] - %(levelname)s - %(message)s"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_formatter)
    if flask_app.config['DEBUG']:
        handler.setLevel(logging.DEBUG)
    else:
        handler.setLevel(logging.INFO)

    flask_app.logger.addHandler(handler)

    register_extensions(flask_app)
    register_api(cnnx_app)

    return flask_app
