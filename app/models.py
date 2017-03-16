from flask_sqlalchemy import SQLAlchemy
from app import create_app 

db = SQLAlchemy(create_app())

class User(db.Model):
	__tablename__='users'
	id=db.Column('id',db.Integer, primary_key = True)
	username=db.Column('username', db.String(30))
	password=db.Column('password', db.String(30))
	admin=db.Column('admin', db.Integer())

	def __init__(self, username, password):
		self.username=username
		self.password=password

	def __repr__(self):
		return '<User %r>' % self.username

class Books(db.Model):
	__tablename__='books'
	id=db.Column('id', db.Integer, primary_key = True)
	title=db.Column('title', db.String(100))
	category=db.Column('category',db.String(50))
	availabilty=db.Column('available', db.String(10))


	def __init__(self, title, category,availabilty):
		self.title=title
		self.category=category
		self.availabilty=availabilty