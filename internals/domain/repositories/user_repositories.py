from internals.domain.models.user import User
from pkg.configs.database import db


class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            return user.to_dict()
        else:
            return None

    @staticmethod
    def get_user_by_username(email_or_username):
        user = User.query.filter_by(username=email_or_username,email=email_or_username).first()
        if user:
            return user.to_dict()
        else:
            return None

    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user, **kwargs):
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()
        return user

    @staticmethod
    def delete_user_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
