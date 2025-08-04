from flask import Flask
from .config import Config
from .extensions import db
from flask_wtf import CSRFProtect


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from .main.routes import main_bp
    app.register_blueprint(main_bp)

    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    db.init_app(app)
    CSRFProtect(app)

    print(app.url_map)

    return app
