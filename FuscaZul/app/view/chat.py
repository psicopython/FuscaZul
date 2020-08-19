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
	if request.method != 'GET':
		@app.sk.on('message')
		def get_msg(dados):
			print(dados)
			current_app.socketio.emit('message',dados)
	
	app.sk.run(app)
	return render_template('chat.html')