import datetime

from pytz import timezone
from pkg.configs.database import db
from pkg.configs.config import Config


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tel = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True), default=datetime.datetime.now(timezone(Config.TZ))
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        default=datetime.datetime.now(timezone(Config.TZ)),
        onupdate=datetime.datetime.now(timezone(Config.TZ)),
    )

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "tel": self.tel,
            "role": self.role,
        }
