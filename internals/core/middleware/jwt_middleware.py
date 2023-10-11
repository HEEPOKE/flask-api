from functools import wraps

from flask import request
import jwt
from pkg.configs.config import Config
from pkg.constants.response_message import ResponseMessages
from internals.core.utils.response import response
from pkg.constants.status import Code
from pkg.constants.service import Service


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return response(
                Code.FAILED,
                Service.AUTH_SERVICE,
                ResponseMessages.TOKEN_MESSING,
                None,
                401,
            )

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return response(
                Code.FAILED,
                Service.AUTH_SERVICE,
                ResponseMessages.TOKEN_EXPIRED,
                None,
                401,
            )
        except jwt.InvalidTokenError:
            return response(
                Code.FAILED,
                Service.AUTH_SERVICE,
                ResponseMessages.TOKEN_INVALID,
                None,
                401,
            )

        return f(data, *args, **kwargs)

    return decorated
