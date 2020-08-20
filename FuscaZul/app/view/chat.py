from flask import (
	redirect, request, url_for,
	jsonify, render_template,
	session, current_app,
)

from app.model.chat import (
	Chat, Mensagem, ImgMsg,
)
from app.model.user import User


def chat(id):
	if not id:
		return redirect('/')
	if not 'user_id' in session:
		return redirect('/')
	user_loc = User.query.filter_by(id=session['user_id']).first()
	user_rec = User.query.filter_by(id=id).first()
	if not user_rec or not user_loc:
		return redirect('/')
		
	user_loc = user_loc.get_user()
	user_rec = user_rec.get_user()
	if request.method == 'POST':
		dados = request.json 
		mensagem = dados['msg']
		user_env = dados['id_user_1']
		user_rec = dados['id_user_2']
		if msg and user_rec and user_env:
			conv1 = Chat.query.filter_by(id_user=user_env).first()
			conv2 = Chat.query.filter_by(id_user=user_rec).first()
			if not conv1:
				conv1 = Chat(id_user1=user_env,id_user2=user_rec)
				current_app.db.session.add(conv1)
				current_app.db.session.commit()
		
			if not conv2:
				conv2 = Chat(id_user2=user_env,id_user1=user_rec)
				current_app.db.session.add(conv2)
				current_app.db.session.commit()
			
			msg1 = Mensagem(
				id_conv=conv1.id,
				id_user1=user_env,
				id_user2=user_rec,
				mensagem=mensagem,
			)
			msg2 = Mensagem(
				id_conv=conv2.id,
				id_user1=user_env,
				id_user2=user_rec,
				mensagem=mensagem,
			)
			current_app.db.session.add_all(msg1,msg2)
			current_app.db.session.commit()
			
			
	return jsonify('Criado!'), 201