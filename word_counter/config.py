import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = "???"
  SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]

class DevelopmentConfig(Config):
  DEBUG = True
  DEVELOPMENT = True

class ProductionCongi(Config):
  DEBUG = False

class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True
