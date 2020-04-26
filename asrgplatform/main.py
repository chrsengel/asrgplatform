from flask import Blueprint
from flask_login import login_required
from asrgplatform import db, logger, login_manager

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/dashboard')
@login_required
def dashboard():
    return 'Dashboard'
