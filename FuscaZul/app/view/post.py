
from app.model.post import Post, ImgPost
from app.model.user import User


from flask import (
	jsonify, flash,
	render_template,
	redirect, request,
	session, current_app,
)




def post():
	# Pegando o user atual (logado)
	## If no estiver loggado, não acessará a página
	if not 'user_id' in session:
		return redirect('/')
	
	## Se tiver um user no cache, irá pegá-lo
	user = User.query.filter_by(id=session['user_id']).first()
	### Se não existir um usuário com esse id,
	### será redirecionado
	if not user:
		session.pop('user_id',None)
		redirect('/')
		
	## se td estiver certo,
	## apenas pega os dados em forma de um json
	user = user.get_user()
	
	# verifica se esta entrando na página
	## ou se já esta enviando o form do poster
	if request.method == 'POST':
		# variáveis globais
		body, imgs, JS, n_img = None, None, False, None
		# Agora é a parte de criação do post
		## verifica se é um Json
		if request.json:
			# pega os dados
			body = request.json('body')
			imgs = request.json('img')
			
				
			
		## Verifica se é um post 
		if request.form:
			
			# pega os dados
			body = request.form['body']
			imgs = request.files.getlist('img')
			
			# verifica se há ao menos um desses dados
		if body or imgs:
			
			#cria um post
			post = Post(
				id_user=user['id'],
				legenda=body,
			)
			current_app.db.session.add(post)
			current_app.db.session.commit()
			
			# verifica se há alguma imagem,
			# só para evitar erro
			if imgs:
				
				# pega a lista de imagens
				# add cada imagem ao db
				for img in imgs:
					
					n_img = ImgPost(
						id_user=user['id'],
						id_post=post.id,
						imagem=img.read(),
					)
					current_app.db.session.add(n_img)
					current_app.db.session.commit()
			if JS:
				return jsonify("Post Criado")
			return redirect('/post/?'+str(n_img.id))
			
		if JS:
			return jsonify({"Erro":"Ao menos um campo deve ser preenchido"})
		flash('Algum campo deve ser preenchido')
	
	return render_template('post.html',user=user)