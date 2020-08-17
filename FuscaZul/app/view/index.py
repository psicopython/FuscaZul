
from flask import (
	render_template,request,
	session,current_app,
	jsonify,
	
)

from app.model.user import User


def index():
	dic_users = {}
	#users = User.query.all()
	users = User.query.filter_by(id=1).first()
	#if len(users) > 1:
	#	for user in users:
	#		dic_users[user.id] = user.get_user()
	#return users.get_user() if not dic_users else dic_users
	user = users.get_user()
	return user