from flask import Flask
from .config import Config
from .extensions import db
from app.routes.main import main_bp
from app.routes.auth import auth_bp
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    CSRFProtect(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
