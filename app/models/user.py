from ..extensions import db


# 定义数据库表 User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(80))
