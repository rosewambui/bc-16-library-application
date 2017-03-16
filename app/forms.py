from flask_wtf import FlaskForm, csrf
from wtforms.csrf.session import SessionCSRF
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired
from datetime import timedelta

class signInForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

	class Meta:
		csrf = True
		csrf_class = SessionCSRF
		csrf_secret = b'EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'
		csrf_time_limit = timedelta(minutes=20)

class signUpForm(FlaskForm):
	#userid = IntegerField('user Id', validators=[DataRequired()])
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	confirm_password = PasswordField(' confirm Password', validators=[DataRequired()])

	class Meta:
		csrf = True
		csrf_class = SessionCSRF
		csrf_secret = b'EPj00jpfj8Gx1SjnyLxwBBSQfnQ9DJYe0Ym'
		csrf_time_limit = timedelta(minutes=20)
#class user(FlaskForm):
