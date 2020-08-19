from flask import (
	Flask, render_template,
	
)
from flask_socketio import SocketIO
from app.model import config_db
from app.socket import config_sk



def create():
	app = Flask(__name__.split('.')[0])
	app.config['SECRET_KEY'] = 'FuSKaZul'
	
	config_db(app)
	config_sk(app)
	
	
	@app.route('/')
	def index():
		return open('app/templates/index.html','r').read()
	
	
	@app.sk.on('message')
	def save_message(data):
		print(type(data['data']['img']))
		app.sk.emit('message',data)
	
	
	return app