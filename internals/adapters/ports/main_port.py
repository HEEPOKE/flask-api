from internals.adapters.ports.user_port import user_port_bp

def init_port(app):
    app.register_blueprint(user_port_bp, url_prefix='/apis')