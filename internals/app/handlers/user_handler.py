from internals.domain.models.user import User
from internals.domain.repositories.user_repositories import UserRepository
from pkg.constants.response_message import ResponseMessages
from internals.core.utils.response import response
from pkg.constants.status import Code
from pkg.constants.service import Service


class UserHandler:
    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_users()
        user_list = [
            {"id": user.id, "username": user.username, "email": user.email}
            for user in users
        ]
        return response(
            Code.SUCCESS,
            Service.USER_SERVICE,
            ResponseMessages.USER_LIST_SUCCESS,
            user_list,
            200,
        )

    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            return response(
                Code.SUCCESS,
                Service.USER_SERVICE,
                ResponseMessages.USER_GET_BY_ID_SUCCESS,
                user,
                200,
            )
        else:
            return response(
                Code.FAILED,
                Service.USER_SERVICE,
                ResponseMessages.USER_GET_BY_ID_FAILED,
                user,
                400,
            )
        
    @staticmethod
    def get_user_by_email_or_username(email_or_username):
        user = UserRepository.get_user_by_email_or_username(email_or_username)
        if user:
            return response(
                Code.SUCCESS,
                Service.USER_SERVICE,
                ResponseMessages.USER_GET_BY_EMAIL_SUCCESS,
                user,
                200,
            )
        else:
            return response(
                Code.FAILED,
                Service.USER_SERVICE,
                ResponseMessages.USER_NOT_FOUND,
                user,
                400,
            )
        

    @staticmethod
    def create_user(user_data):
        username = user_data.get("username")
        email = user_data.get("email")
        password = user_data.get("password")
        tel = user_data.get("tel")

        user = User(username=username, email=email, password=password, tel=tel)
        created_user = UserRepository.create_user(user)

        return response(
            Code.SUCCESS,
            Service.USER_SERVICE,
            ResponseMessages.USER_CREATE_SUCCESS,
            created_user,
            201,
        )

    @staticmethod
    def update_user(user_id, user_data):
        user = UserRepository.get_user_by_id(user_id)

        if not user:
            return response(
                Code.FAILED,
                Service.USER_SERVICE,
                ResponseMessages.USER_NOT_FOUND,
                None,
                404,
            )

        updated_user = UserRepository.update_user(user, **user_data)

        return response(
            Code.SUCCESS,
            Service.USER_SERVICE,
            ResponseMessages.USER_UPDATE_SUCCESS,
            updated_user,
            200,
        )

    @staticmethod
    def delete_user(user_id):
        deleted = UserRepository.delete_user_by_id(user_id)

        if deleted:
            return response(
                Code.SUCCESS,
                Service.USER_SERVICE,
                ResponseMessages.USER_DELETED_SUCCESS,
                deleted,
                200,
            )
        else:
            return response(
                Code.FAILED,
                Service.USER_SERVICE,
                ResponseMessages.USER_NOT_FOUND,
                None,
                404,
            )
