from pkg.configs.database import db


class AuthRepository:
    @staticmethod
    def register(user):
        db.session.add(user)
        db.session.commit()
        return user
