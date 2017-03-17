from flask_sqlalchemy import SQLAlchemy
from app import create_app

db = SQLAlchemy(create_app())

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    admin = db.Column(db.Boolean)
    borrows = db.relationship('Borrow', backref='user', lazy='dynamic')

    def __init__(self, username, password, admin=False):
        self.username = username
        self.password = password
        self.admin = admin


class Category(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    books = db.relationship('Book', backref='category', lazy='dynamic')

    def __init__(self, title):
        self.title = title


class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    availabilty = db.Column(db.String(10))
    borrows = db.relationship('Borrow', backref='book', lazy='dynamic')

    def __init__(self, title, category_id):
        self.title = title
        self.category_id = category_id


class Borrow(db.Model):

    __tablename__ = 'borrows'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    returned = db.Column(db.Boolean, default=False)
