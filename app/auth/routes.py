from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user
from app.models.user import User
from app.extensions import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.username.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            print("用户名已存在")
            flash("用户名已存在")
        else:
            new_user = User()
            new_user.set_info(form.username.data, form.email.data, form.phone.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            print("注册成功，请登录")
            flash("注册成功，请登录")
            return redirect(url_for('auth.login'))
    else:
        print("注册失败")
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            print("登录成功")
            return redirect(url_for('main.index'))
        else:
            print("登陆失败")
            flash("用户名或密码错误")
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("已退出登录")
    return redirect(url_for('auth.login'))
