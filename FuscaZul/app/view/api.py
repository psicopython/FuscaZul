from flask import (
	jsonify,
)

from app.model.user import User


def apiUser(id):
	user = User.query.filter_by(id=id).first()
	if user:
		user = user.get_user()
		return jsonify(user),200
	return jsonify('user not found'),404