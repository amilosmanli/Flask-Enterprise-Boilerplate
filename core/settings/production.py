from core.settings.base import Config


class ProductionConfig(Config):
    """ Configuration class for site production environment """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgres:///template1'