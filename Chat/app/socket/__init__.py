from flask_socketio import SocketIO


sk = SocketIO()

def config_sk(app):
	sk.init_app(app)
	app.sk = sk