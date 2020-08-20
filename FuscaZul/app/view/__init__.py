
from flask import Blueprint


from .post import post

from .index import index

from .login import login, logout
from .cadastro import cadastro


from .api import apiUser

bp = Blueprint(
	'webui',__name__
)


bp.add_url_rule(
	'/',
	methods=["GET"],
	view_func=index,
	endpoint='index'
)

bp.add_url_rule(
	'/post/',
	methods=["GET","POST"],
	view_func=post,
	endpoint='post'
)



bp.add_url_rule(
	'/cadastro/',
	methods=["GET","POST"],
	view_func=cadastro,
	endpoint='cadastro'
)

bp.add_url_rule(
	'/login/',
	methods=["GET","POST"],
	view_func=login,
	endpoint='login'
)


bp.add_url_rule(
	'/logout/',
	methods=["GET"],
	view_func=logout,
	endpoint='logout'
)



bp.add_url_rule(
	'/post/',
	methods=["GET","POST"],
	view_func=post,
	endpoint='post'
)


bp.add_url_rule(
	'/api/user/<int:id>/',
	methods=["GET","POST"],
	view_func=apiUser,
	endpoint='apiUser'
)



def config_vw(app):
	app.register_blueprint(bp)