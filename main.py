import os
from flask import Flask
from pkg.configs.database import db, init_db, migrate_db
from pkg.configs.config import config_app

def create_app():
    app = Flask(__name__)

    environment = os.environ.get("FLASK_ENV")
    app.config.from_object(config_app[environment])

    init_db(app)
    migrate_db(app, db)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
