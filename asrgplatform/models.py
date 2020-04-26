from asrgplatform import db
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
