from flask import Blueprint, request
from flask_cors import cross_origin
from internals.app.handlers.user_handler import UserHandler

user_port_bp = Blueprint("user_port", __name__)


@user_port_bp.route("/users/list", methods=["GET"])
@cross_origin()
def get_all_users():
    users = UserHandler.get_all_users()
    return users


@user_port_bp.route("/users/find/<int:user_id>", methods=["GET"])
@cross_origin()
def get_user_by_id(user_id):
    user = UserHandler.get_user_by_id(user_id)
    return user


@user_port_bp.route("/users/find", methods=["GET"])
@cross_origin()
def get_user_by_email_or_username():
    email_or_username = request.args.get("email_or_username")
    user = UserHandler.get_user_by_email_or_username(email_or_username)
    return user


@user_port_bp.route("/users/create", methods=["POST"])
@cross_origin()
def create_user():
    data = request.get_json()
    user = UserHandler.create_user(data)
    return user


@user_port_bp.route("/users/update/<int:user_id>", methods=["PUT"])
@cross_origin()
def update_user(user_id):
    data = request.get_json()
    return UserHandler.update_user(user_id, data)


@user_port_bp.route("/users/delete/<int:user_id>", methods=["DELETE"])
@cross_origin()
def delete_user(user_id):
    return UserHandler.delete_user(user_id)
