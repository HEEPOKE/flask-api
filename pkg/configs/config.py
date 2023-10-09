import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = False
    FLASK_RUN_PORT = int(os.environ.get("FLASK_RUN_PORT"))
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@localhost/{os.environ["DB_NAME"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_app = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}