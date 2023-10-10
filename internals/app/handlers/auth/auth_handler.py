import bcrypt
from internals.app.services.auth_service import AuthServices
from pkg.constants.response_message import ResponseMessages
from internals.core.utils.response import response
from pkg.constants.status import Code
from pkg.constants.service import Service


class AuthHandler:
    @staticmethod
    def login(data):
        users = AuthServices.login(data.username_or_email)

        if users:
            if bcrypt.checkpw(users.password.encode("utf-8"), data.password):
                return response(
                    Code.SUCCESS,
                    Service.AUTH_SERVICE,
                    ResponseMessages.USER_LIST_SUCCESS,
                    users,
                    200,
                )
            else:
                return response(
                    Code.FAILED,
                    Service.AUTH_SERVICE,
                    ResponseMessages.AUTH_PASSWORD_INCORRECT,
                    None,
                    400,
                )
        else:
            return response(
                Code.FAILED,
                Service.AUTH_SERVICE,
                ResponseMessages.AUTH_LOGIN_FAILED,
                None,
                400,
            )
        