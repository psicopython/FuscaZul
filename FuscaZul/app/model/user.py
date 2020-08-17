from . import db,ma
from .post import Post

from cryptography.fernet import Fernet
KEY = b'_1M5mGNigr6IH0xljq4QPZFDfWwnWR99tOvIaWUj-CA='

import datetime

from werkzeug.security import (
	generate_password_hash as gph,
	check_password_hash as cph,
)




class User(db.Model):
	
	__tablename__ = 'user'
	
	id = db.Column(db.Integer,primary_key=True)
	tel = db.Column(db.String(32))
	nasc = db.Column(db.Date)
	nome = db.Column(db.Text(convert_unicode=True),nullable=False)
	email = db.Column(db.String(128),unique=True,nullable=False)
	senha = db.Column(db.Text,nullable=False)
	create = db.Column(db.DateTime,nullable=False)
	post_img = db.Column(db.Integer)
	
	
	def _get_data(self):
		return datetime.datetime.today()
	
	
	def encrypt(self,dado):
		enc = Fernet(KEY)
		return enc.encrypt(bytes(dado,'utf-8'))
	
	def decrypt(self,dado):
		dec = Fernet(KEY)
		return dec.decrypt(bytes(dado)).decode('utf-8')
	
	
	
	def hash_senha(self, senha):
		return gph(senha)
		
	def check_senha(self, senha):
		return cph(self.senha, senha)
	
	
	def get_user(self):
		post = Post.query.filter_by(id=self.post_img).first()
		return {
			"id": self.id,
			"tel": self.tel,
			"nasc": self.nasc,
			"nome": self.nome,
			"email": self.email,
			"create": self.create,
			"img_post": post.get_post() if post else None,
		}
	
	
	def __init__(
		self, tel, nas, nome,
		email, senha, post_img
		):
		
		self.tel = tel
		self.nasc = nas
		self.nome = nome
		self.email = email
		self.senha = self.hash_senha(senha)
		self.create = self._get_data()
		self.post_img = post_img
		
		
	
	def __repr__(self):
		return f"<User id:{self.id}|| nome:{self.nome}>"


class UserSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = User 
	


"""
class UserImg(db.Model):
	
	__tablename__='userImg'
	
	id = db.Column(db.Integer,primary_key=True)
	foto = db.Column(db.BLOB,nullable=False)
	data = db.Column(db.Date,nullable=False)
	id_post = db.Column(db.Integer,nullable=False)
	id_user = db.Column(db.Integer,nullable=False)
	
"""