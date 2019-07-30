"""
Face Recognition Service
Server configuration

Copyright (c) 2019 Nguyen Thanh Thien Phuc
Licensed under the MIT License (see LICENSE for details)
"""
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """
    Base configuration
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_TRACK_MODIFICATION = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(BaseConfig):
    """
    Development configuration
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'database-dev.sqlite')


class TestingConfig(BaseConfig):
    """
    Testing configuration
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(BaseConfig):
    """
    Production configuration
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'database.sqlite')


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}
