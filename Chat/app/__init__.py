from flask import (
	redirect, request, url_for,
	jsonify, render_template,
	session, current_app,Flask
)

import requests

from app.model.chat import (
	Chat, Mensagem, ImgMsg,
)


from flask_socketio import SocketIO
from app.model import config_db
from app.socket import config_sk



def create():
	app = Flask(__name__.split('.')[0])
	
	app.config['SECRET_KEY'] = 'FuSKaZul'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['ENV'] = 'development'
	app.config['DEBUG'] = True
	
	
	config_db(app)
	config_sk(app)
	
	
	@app.route('/chat/<int:id>/<int:id2>/')
	def index(id,id2):
		msgs = None
		
		url = 'http://localhost:5000/api/user/'
		user = requests.get(url+str(id)).json()
		user2 = requests.get(url+str(id2)).json()
		conv = Chat.query.filter_by(user1=user['id'],user2=user2['id']).first()
		if conv:
			msgs = Mensagem.query.filter_by(id_conv=conv.id).order_by(current_app.db.desc('id')).limit(15).all()
			msgs = msgs[::-1]
		return render_template('index.html',user=user,user2=user2,msgs=msgs)
	
	
	def chat(dados={}):
		if not dados:
			return False
			
		n_mensagem = dados['msg']
		user_env = int(dados['id_user1'])
		user_rec = int(dados['id_user2'])
		
		if n_mensagem and user_rec and user_env:
			conv1 = Chat.query.filter_by(
				user1=user_env,
				user2=user_rec).first()
			
			
			conv2 = Chat.query.filter_by(
				user1=user_rec,
				user2=user_env).first()
			
			if not conv1:
				conv1 = Chat(user_env, user_rec)
				current_app.db.session.add(conv1)
				current_app.db.session.commit()
				
			if not conv2:
				conv2 = Chat(user_rec, user_env)
				current_app.db.session.add(conv2)
				current_app.db.session.commit()
			
			msg1 = Mensagem(
				id_conv=conv1.id,
				id_user1=user_env,
				id_user2=user_rec,
				mensagem=n_mensagem,
			)
			msg2 = Mensagem(
				id_conv=conv2.id,
				id_user1=user_env,
				id_user2=user_rec,
				mensagem=n_mensagem,
			)
			current_app.db.session.add_all([msg1,msg2])
			current_app.db.session.commit()
			return msg1
	
	
	@app.sk.on('message')
	def save_message(data):
		if data:
			msg = chat(data)
			msg = msg.get_msg()
			app.sk.emit('message',msg)
	
	
	return app
