from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, ValidationError, RadioField, BooleanField, SubmitField, IntegerField, FormField, validators, PasswordField, SelectField
from wtforms.validators import DataRequired, Required, Email


class SignupForm(FlaskForm):
    email = StringField('Email', [Email("Not a valid email!"), validators.required(), validators.length(min=5, max=45)])
    password = PasswordField('Password', [DataRequired(message="Please enter a password"), validators.required(), validators.length(min=8, max=80)])


class LoginForm(FlaskForm):
    email = StringField('Email', [Email("Not a valid email!"), validators.required(), validators.length(min=5, max=45)])
    password = PasswordField('Password', [validators.required(), validators.length(min=8, max=80)])
