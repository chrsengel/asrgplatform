from asrgplatform import db
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import bcrypt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def set_password(self, password):
        """Set a new password."""
        self.password = bcrypt.hashpw(password, bcrypt.gensalt(6)).decode("utf-8", "ignore")

    def check_password(self, password):
        """Check the hashed password."""
        return bcrypt.checkpw(password, self.password.encode())
