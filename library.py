from flask import render_template, flash, request
from app import create_app
from app.forms import *
from app.models import User, db

app = create_app()

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/sign_up",  methods=["GET", "POST"])
def sign_up():
	form  = signUpForm(request.json)
	print(" >>>>>>>", request.json)
	if form.validate_on_submit():
		password = form.password.data.strip()
		
		if ((password == form.confirm_password.data) 
			and len(password) > 1):
			user = User(username=form.username.data,
				password=password)
			db.session.add(user)
			db.session.commit()
			flash("Thanks for creating an account")
			return render_template('user.html')
			#return redirect(url_for('user'))
		else:
			flash('password was either less than 5 character or wasn\'t equal')
			return render_template('sign_up.html', form=form)
	return render_template('sign_up.html', form=form)

@app.route("/sign_in",  methods=["POST", "GET"])
def sign_in():
	form = signInForm(request.form)
	print('methods >>>>>', request.form)
	if form.validate() and request.method == 'POST':
		logged_user = User.query.filter_by(
			username=form.username.data, 
			password=form.password.data).first()
		print ('>>>>>', logged_user)
		if logged_user != "":
			flash("You logged in successfully")
			return render_template('user.html')
		else:
			flash("You username or password was incorrect")
			return render_template('sign_in.html', form=form)
	return render_template('sign_in.html', form=form)

@app.route("/admin")
def admin():
	return render_template('admin.html')

@app.route("/user",  methods=["POST"])
def user():
	return render_template('user.html')
	



if __name__ == "__main__":
	app.run()