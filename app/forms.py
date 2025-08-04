# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('login')


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm = PasswordField('confirm', validators=[DataRequired(), EqualTo('password')])
    email = StringField('email', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])

    submit = SubmitField('register')
