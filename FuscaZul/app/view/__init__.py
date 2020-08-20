
from flask import Blueprint


#from .index import index
from .post import post

from .post import post

from .login import login, logout
from .login import login, logout
from .cadastro import cadastro


bp = Blueprint(
	'webui',__name__
)


"""
bp.add_url_rule(
	'/',
	methods=["GET"],
	view_func=index,
	endpoint='index'
)"""

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



def config_vw(app):
	app.register_blueprint(bp)