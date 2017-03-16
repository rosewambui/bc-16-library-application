from flask import Flask

app = Flask(__name__)
app.secret_key = 'development key'

def create_app():
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////libapp.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS' ]= False 
	app.config['DEBUG']=True
	return app