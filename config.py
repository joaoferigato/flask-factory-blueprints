import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

    SECRET_KEY = os.getenv('SECRET_KEY')  # python -c 'import secrets; print(secrets.token_hex())'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    MAIL_SUPPRESS_SEND = True


class ProductionConfig(Config):
    DEBUG = True
