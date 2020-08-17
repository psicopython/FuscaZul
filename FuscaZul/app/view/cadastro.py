
from flask import (
	session, current_app, redirect, 
	render_template, jsonify,
	request,
)

from app.model.user import User
from app.model.post import Post, ImgPost

import datetime


def cadastro():
	if 'user_id' in session:
		return redirect('/')
	
	if request.method == 'POST':
		
		post , nome, email, senha, img, nas, tel = None,None,None,None,None,None,None
		
		if request.json:
			n_user = request.json['user']
			
			nome = n_user['nome']
			email = n_user['email']
			senha = n_user['senha']
			img = n_user['imagem'] if n_user['imagem'] else None
			nas = n_user['nas'] if n_user['nas'] else None
			tel = n_user['tel'] if n_user['tel'] else None
		
		
		
		if request.form:
			
			img = request.files.get('imagem')
			print(img)
			nas = request.form['nas']
			tel = request.form['tel']
			nome = request.form['nome']
			email = request.form['email']
			senha = request.form['senha']
		
		
		
		if nas:
			nas = datetime.datetime.strptime(nas,'%Y-%m-%d').date()
		
		new_user = User(
			nome=nome,email=email,
			senha=senha,nas=nas,
			tel=tel,post_img=None
		)
		current_app.db.session.add(new_user)
		current_app.db.session.commit()
		
		if img:
			post = Post(
				id_user=new_user.id, legenda=''
			)
			current_app.db.session.add(post)
			current_app.db.session.commit()
			
			img_post = ImgPost(
				id_user=new_user.id,
				id_post=post.id,
				imagem=img.read() ,
			)
			current_app.db.session.add(img_post)
			current_app.db.session.commit()
			print(img_post.id)
			
			User.query.filter_by(id=new_user.id).update({'post_img':img_post.id})
			current_app.db.session.commit()
			print('///')
		
		return jsonify("ok")
	else:
		return render_template('cad.html')