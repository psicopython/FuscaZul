
from flask import (
	jsonify, flash,
	redirect, request,
	session, current_app,
	render_template,
)

from app.model.user import User

def logout():
	session.pop('user_id',None)
	return redirect('/')
	
def login():
	email, senha, JS = None , None, False
	# Verificaçao: Credenciais no cache 
	if 'user_id' in session:
		user = User.query.filter_by(id=session['user_id']).first()
		## se houver um usuário equivalente
		## ao id no cache, será redirecionado ao index
		if user:
			redirect('/')
			
		## Senão excluirá o id que esta no cache
		## e continuará o processo de login
		session.pop('user_id',None)
		
	# Se estiverem enviando os dados para o login:
	if request.method == 'POST':
		# Declaração de variáveis globais
		
		
		# se estiverem enviando um um formulário
		if request.form:
			email = request.form['email']
			senha = request.form['senha']
			 
		# se estiverem enviando um json
		if request.json:
			email = request.json('email')
			senha = request.json('senha')
			JS = True
			
		# verifica se há um usuário com esse login
		user = User.query.filter_by(email=email).first()
		if user:
			
			# se as senhas coincidem
			if user.check_senha(senha):
				session['user_id'] = user.id
				return redirect('/')
				
			# js é a Verificaçao se é um json ou form
			if JS:
				return {"Erro":"Credenciais Inválidas"}
			flash(' senha Inválida!')
		
		else:
			# js é a Verificaçao se é um json ou form
			if JS:
				return {"Erro":"Credenciais Inválidas"}
			flash('Email Inválido!')
	
	# se for um GET 
	return render_template('login.html')