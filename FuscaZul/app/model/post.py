from app.model import db

from base64 import b64encode
from datetime import datetime


class Post(db.Model):
	
	__tablename__ = 'post'
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	legenda = db.Column(db.Text)
	id_user = db.Column(db.Integer,nullable=False)
	
	def _get_data(self):
		return datetime.now()
		
		
	def __init__(self,id_user,legenda):
		
		self.id_user = id_user
		self.legenda = legenda
		self.data = self._get_data()
		
	
	def get_post(self):
		
		all_img = ImgPost.query.filter_by(id_post=self.id).all()
		imgs = []
		for imagem in all_img:
			imgs.append(imagem.get_imgPost())
			
		return {
			"id": self.id,
			"data": self.data,
			"id_user": self.id_user,
			"imagens":imgs,
			"legenda": self.legenda,
		}
	
	
	def __repr__(self):
		return f"<Post id:{self.id}>"
	



class ImgPost(db.Model):
	
	__tablename__ = 'Imgpost'
	
	id = db.Column(db.Integer,primary_key=True)
	data = db.Column(db.DateTime,nullable=False)
	imagem = db.Column(db.BLOB)
	id_user = db.Column(db.Integer,nullable=False)
	id_post = db.Column(db.Integer,nullable=False)
	
	def _get_data(self):
		return datetime.now()
		
		
	def __init__(self,id_user, id_post, imagem):
		self.id_user = id_user
		self.id_post = id_post
		self.imagem = imagem
		self.data = self._get_data()

	
	def get_imgPost(self):
		
		return {
			"id": self.id,
			"data": self.data,
			"id_user": self.id_user,
			"id_post": self.id_post,
			"imagem": b64encode(self.imagem).decode('ascii'),
		}
	
	
	def __repr__(self):
		return f"<Imagem Post=>{self.id}>"