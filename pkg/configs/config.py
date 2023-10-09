import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_DEBUG = 0
    FLASK_RUN_PORT = int(os.environ.get("FLASK_RUN_PORT"))
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@localhost/{os.environ["DB_NAME"]}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    TZ = os.environ.get("TIME_ZONE")


class DevelopmentConfig(Config):
    FLASK_DEBUG = 1


class ProductionConfig(Config):
    FLASK_DEBUG = 0


config_app = {"development": DevelopmentConfig, "production": ProductionConfig}
