from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////libapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ]= False 
db = SQLAlchemy(app)


class User(db.Model):
	__tablename__='users'
	id=db.Column('user_id',db.Integer, primary_key = True)
	username=db.Column('username', db.String(30))
	password=db.Column('password', db.String(30))
	is_admin=db.Column('admin', db.Integer())

	def __init__(id, username, password):
		self.id=id
		self.username=username
		self.password=password

	def __repr__(self):
		return '<User %r>' % self.username

class Books(db.Model):
	__tablename__='books'
	id=db.Column('book_id', db.Integer, primary_key = True)
	title=db.Column('title', db.String(100))
	category=db.Column('category',db.String(50))
	#is_available=Column('available', Integer(3))


	def __init__(self, id, title, category):
		self.id=id
		self.title=title
		self.category=category
		#self.is_available=is_available
