import datetime
import jwt

from pytz import timezone

from pkg.configs.config import Config


def generate_token(data):
    payload = {
        "data": data,
        "exp": datetime.datetime.now(timezone(Config.TZ)) + datetime.timedelta(hours=1),
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
    return token


def verify_token(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
