from flask import Flask, redirect, url_for
from .config import Config
from .extensions import db
from .models.user import User
from flask_wtf import CSRFProtect
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    @app.route('/')
    def index():
        return redirect(url_for('main.index'))

    from .main.routes import main_bp
    app.register_blueprint(main_bp)

    from .auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.index'

    @login_manager.user_loader
    def load_user(user_id):
        user = User.query.get(int(user_id))
        return user

    db.init_app(app)
    CSRFProtect(app)

    with app.app_context():
        db.create_all()

    return app
