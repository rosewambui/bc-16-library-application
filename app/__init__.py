from flask import Flask
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.secret_key = 'development key'

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ]= False
    app.config['DEBUG']=True
    app.config['WTF_CSRF_CHECK_DEFAULT'] = False
    csrf = CsrfProtect()

    csrf.init_app(app)
    return app
