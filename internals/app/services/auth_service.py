
from internals.domain.models.user import User


class AuthServices:
    @staticmethod
    def login(username_or_email):
        user = User.query.filter_by(username=username_or_email,email=username_or_email).first()
        return user
