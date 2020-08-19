from flask_socketio import SocketIO

socket = SocketIO()

def config_sk(app):
	socket.init_app(app)
	app.sk = socket