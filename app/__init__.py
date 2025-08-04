from flask import Flask
from .config import Config
from .extensions import db
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config.from_object(Config)

    # from app.main.routes import main_bp
    from app.auth.routes import auth_bp
    # app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    db.init_app(app)
    CSRFProtect(app)

    return app
