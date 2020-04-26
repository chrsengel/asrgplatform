from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, login_user
from asrgplatform import db, logger, login_manager
from asrgplatform.forms import SignupForm, LoginForm
from asrgplatform.models import User
from wtforms import StringField, TextAreaField, ValidationError, RadioField, BooleanField, SubmitField, IntegerField, FormField, validators, PasswordField, SelectField
from wtforms.validators import Required
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import bcrypt


log = logger.child(context="auth")

auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('auth.login'))


@auth.route("/login", methods=("GET", "POST"))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        pw = form.password.data.encode()

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(pw):
            log.info("[+] logged in user")
            login_user(user)
            return redirect(url_for("main.dashboard"))

        return redirect(url_for('auth.login'))
    return render_template("login.html", form=form)


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = form.email.data
        pw = form.password.data.encode()
        user = User.query.filter_by(email=email).first()

        if user:
            log.info("[-] email is already taken")
            return redirect(url_for('auth.signup'))

        pw_hash = bcrypt.hashpw(pw, bcrypt.gensalt(6)).decode("utf-8", "ignore")
        new_user = User(email=email, password=pw_hash)

        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template("signup.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth.login'))
