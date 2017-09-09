# -*- coding: utf-8 -*-
from core.settings.base import Config


class DevelopmentConfig(Config):
    """ Configuration class for site development environment """

    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgres:///test_boilerplate'