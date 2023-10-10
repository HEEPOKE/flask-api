from internals.adapters.ports.user_port import user_port_bp
from internals.adapters.ports.auth.auth_port import auth_port_bp


def init_port(app):
    app.register_blueprint(auth_port_bp, url_prefix="/apis")
    app.register_blueprint(user_port_bp, url_prefix="/apis")
