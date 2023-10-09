import os
from flask import Flask
from pkg.configs.database import init_db
from pkg.configs.config import config_app

app = Flask(__name__)

environment = os.environ.get("FLASK_ENV")

app.config.from_object(config_app[environment])

init_db(app)

if __name__ == '__main__':
    app.run()
