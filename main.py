import os
from flask import Flask
from flask_cors import CORS
from internals.adapters.ports.main_port import init_port
from pkg.configs.database import db, init_db, migrate_db
from pkg.configs.config import config_app


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"/apis/*": {"origins": "*"}})

    environment = os.environ.get("FLASK_ENV")
    app.config.from_object(config_app[environment])
    app.config["CORS_HEADERS"] = "Content-Type"

    init_db(app)
    migrate_db(app, db)

    init_port(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
