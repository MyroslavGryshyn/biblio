import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIR = ''.join([PROJECT_ROOT + '/' + 'src/', 'client'])
STATIC_DIR = ''.join([PROJECT_ROOT + '/' + 'src/', 'client'])

SQLALCHEMY_DATABASE_URI = ''.join(['sqlite:///', PROJECT_ROOT + '/', 'biblio.db'])
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'sdfgsdgsfasfdasdf23423wd23dfasfd'


class BaseConfig():
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = SQLALCHEMY_TRACK_MODIFICATIONS
    project_root = PROJECT_ROOT
    template_dir = TEMPLATE_DIR
    static_folder = STATIC_DIR


class Config(BaseConfig):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    secret_key = SECRET_KEY


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
