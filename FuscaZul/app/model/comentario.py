from app.model import db

from app.model.user import User


class Comentario(db.Model):
	
	__tablename__ = 'comentario'
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	id_user = db.Column(db.Integer,nullable=False)
	id_post = db.Column(db.Integer,nullable=False)
	comentario = db.Column(db.Text)
	imagem = db.Column(db.BLOB)
	
	
	def _get_data(self):
		return datetime.datetime.now()
		
		
	def __init__(self, id_user,
			comentario, imagem):
		
		self.id_user = id_user
		self.id_post = id_post
		self.imagem = imagem.read()
		self.Comentario = comentario
		self.data = self._get_data()
		
		
	def _get_comm(self):
		
		user = User.query.filter_by(id=self.id_user).first()
		return {
			"id": self.id,
			"data": self.data,
			"id_user": self.id_user,
			"username": user.nome,
			"id_post": self.id_post,
			"comentario": self.comentario,
			"imagem": self.imagem,
		}
		
	def __repr__(self):
		return f"<Comentário: n°{self.id}>"