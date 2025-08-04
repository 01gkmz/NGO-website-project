from flask import Blueprint, request, render_template, redirect, url_for

main_bp = Blueprint('main', __name__)


@main_bp.route('/index')
def index():
    return render_template('main/index.html')
