from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField 
from wtforms.validators import DataRequired

class signInForm(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])

class signUpForm(FlaskForm):
	#userid = IntegerField('user Id', validators=[DataRequired()])
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	confirm_password = PasswordField(' confirm Password', validators=[DataRequired()])
#class user(FlaskForm):
