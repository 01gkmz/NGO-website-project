from flask import Blueprint, render_template, redirect, url_for, flash, session
from app.forms import RegisterForm, LoginForm
from app.models.user import User
from app.extensions import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/register')
def register():
    print("hello")
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash("用户名已存在")
        else:
            new_user = User(username=form.username.data, email=form.email_addr.data, phone=form.phone_number.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash("注册成功，请登录")
            return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth_bp.route('/login')
def login():
    print("good")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            flash("登录成功")
            return redirect(url_for('main.home'))
        else:
            flash("用户名或密码错误")
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("已退出登录")
    return redirect(url_for('auth.login'))
