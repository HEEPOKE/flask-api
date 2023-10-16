from flask import Blueprint, request
from flask_cors import cross_origin
from internals.app.handlers.auth.auth_handler import AuthHandler
from internals.app.handlers.user_handler import UserHandler

auth_port_bp = Blueprint("auth_port", __name__)


@auth_port_bp.route("/auth/login", methods=["POST"])
@cross_origin()
def login():
    data = request.get_json()
    auth = AuthHandler.login(data)
    return auth


@auth_port_bp.route("/auth/register", methods=["POST"])
@cross_origin()
def register():
    data = request.get_json()
    auth = UserHandler.create_user(data)
    return auth


@auth_port_bp.route("/auth/logout", methods=["GET"])
@cross_origin()
def logout():
    token = request.headers.get("Authorization")
    auth = AuthHandler.logout(token)
    return auth
