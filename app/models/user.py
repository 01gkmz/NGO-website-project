from ..extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# 定义数据库表 User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(80))
    phone = db.Column(db.String(80))

    def set_info(self, username, email, phone):
        self.username = username
        self.email = email
        self.phone = phone

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
