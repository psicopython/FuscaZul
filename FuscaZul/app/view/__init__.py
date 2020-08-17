
from flask import Blueprint


from .index import index
from .cadastro import cadastro


bp = Blueprint(
	'webui',__name__
)

bp.add_url_rule('/',methods=["GET"],
	view_func=index,endpoint='index'
)

bp.add_url_rule('/cadastro/',methods=["GET","POST"],
	view_func=cadastro,endpoint='cadastro'
)



def config_vw(app):
	app.register_blueprint(bp)