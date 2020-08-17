

#import os

def config(app):
	
	app.config['SECRET_KEY'] = 'xatubaORchatuba'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql'
	app.template_folder = 'front/templates'
	app.static_folder = 'front/static/'