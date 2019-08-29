import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def make_dir_if_not_exist(dir):
    os.makedirs(dir, exist_ok=True)


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'TFYtRmFjZS1XZWItU2VydmljZQ=='
    DEBUG = False
    ERROR_404_HELP = False
    FILE_ALLOWED = ['image/png', 'image/jpeg']
    STORAGE = os.getenv('STORAGE') or os.path.join(BASE_DIR, 'storage')
    make_dir_if_not_exist(STORAGE)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database-dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database-test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')


config = {'dev': DevelopmentConfig,
          'test': TestingConfig,
          'prod': ProductionConfig,
          'default': DevelopmentConfig}

key = BaseConfig.SECRET_KEY
