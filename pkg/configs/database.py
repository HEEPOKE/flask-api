from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    db.init_app(app)
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'options': '-c timezone=Asia/Bangkok'}}


def migrate_db(app,db):
    migrate.init_app(app, db)
    