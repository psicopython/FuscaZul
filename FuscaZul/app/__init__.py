from flask import Flask

from .config import config
from .model  import config_db
from .view   import config_vw
from .websocket   import config_sk


def create():
	
	app = Flask(__name__.split('.')[0])

	config(app)
	config_db(app)
	config_vw(app)
	config_sk(app)
	
	return app