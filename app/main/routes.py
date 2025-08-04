from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, url_prefix='/main')


@main_bp.route('/index')
def index():
    print("Hello")
    return render_template('index.html')
