
from flask import (
	render_template,request,
	session,current_app,
	jsonify,redirect,
)

from app.model.user import User
from app.model.post import Post



def index():
	dic_users, user, posts = {}, None, None
	user = User.query.filter_by(id=session['user_id']).first()
	if user:
		user = user.get_user()
	else:
		session.pop('user_id',None)
		return redirect('/login/')
	posts = Post.query.all()
	poste = []
	if posts:
		for post in posts:
			poste.append(post.get_post())
	return render_template('index.html',user=user,posts=poste)
