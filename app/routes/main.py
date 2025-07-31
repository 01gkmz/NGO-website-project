from flask import Flask, request, render_template
from app.models.user import db, User
from . import main_bp


@main_bp.route('/')
def index():
    return render_template('index2.html')


@main_bp.route('/main.upload', methods=['POST', 'GET'])
def upload():
    full_name = request.form.get('name')
    email_addr = request.form.get('email')
    phone_num = request.form.get('phone')

    new_user = User(name=full_name, email=email_addr, phone=phone_num)
    db.session.add(new_user)
    db.session.commit()

    print(f"Received name: {full_name}, email: {email_addr}, phone: {phone_num}")

    return render_template('success-page.html')


@main_bp.route('/main.show')
def show():
    users = User.query.all()
    return '<br>'.join([f'{user.name} - {user.email} - {user.phone}' for user in users])

