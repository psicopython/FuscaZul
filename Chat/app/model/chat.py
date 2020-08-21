from . import db

from datetime import datetime

from cryptography.fernet import Fernet
KEY = b'REI53OwhhWL7M0MAs2qRvagpR-E0WPlOW5QJglUkPCc='



class Chat(db.Model):
	
	__tablename__="chat"
	
	id = db.Column(db.Integer,primary_key=True)
	user1 = db.Column(db.Integer,nullable=False)
	user2 = db.Column(db.Integer,nullable=False)
	
	
	
	def get_conv(self):
		return {
			"id_conv": self.id,
			"user_1": self.user1,
			"user_2":self.user2,
		}
		
	def __init__(self,user1,user2):
		
		self.user1 = user1
		self.user2 = user2
	


class Mensagem(db.Model):
	
	__tablename__="mensagem"
	
	id = db.Column(db.Integer,primary_key=True)
	id_env = db.Column(db.Integer,nullable=False)
	id_rec = db.Column(db.Integer,nullable=False)
	id_conv  = db.Column(db.Integer,nullable=False)

	data = db.Column(db.DateTime,nullable=False)
	mensagem = db.Column(db.Unicode)
	
	
	def encrypt(self,msg):
		enc = Fernet(KEY)
		return enc.encrypt(bytes(msg,'utf-8'))
		
		
	def decrypt(self,msg):
		dec = Fernet(KEY)
		return dec.decrypt(msg).decode('utf-8')
	
	
	def get_msg(self):
		
		return {
			"id_msg": self.id,
			"id_conv": self.id_conv,
			"id_user1": self.id_env,
			"id_user2":self.id_rec,
			"msg":self.decrypt(self.mensagem),
			"data":str(self.data)[:19],
			
		}
	
	
	def _get_data(self):
		return datetime.now()
		
	def __init__(self,id_conv,id_user1,id_user2, mensagem):
		
		self.id_env = id_user1
		self.id_rec = id_user2
		self.id_conv = id_conv
		self.data = self._get_data()
		self.mensagem = self.encrypt(mensagem)




class ImgMsg(db.Model):
	
	__tablename__="imgMensagem"
	
	id = db.Column(db.Integer,primary_key=True)
	id_msg = db.Column(db.Integer)
	id_conv = db.Column(db.Integer)
	
	imagem = db.Column(db.BLOB)
	
	
	def __init__(self,id_msg,id_conv,imagem):
		
		self.id_msg = id_msg
		self.id_conv = id_conv
		self.imagem = imagem
	
	def get_imgMsg(self):
		return {
			"id_imgMsg": self.id,
			"id_conv": self.id_conv,
			"id_msg": self.id_msg,
			"imagem": self.imagem,
		}