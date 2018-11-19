from init_app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from passlib.hash import argon2

db = SQLAlchemy(app)
class Post(db.Model):
	id = db.Column(db.Integer, index=True, primary_key=True, unique=True)
	main_image = db.Column(db.String)
	title = db.Column(db.String)
	url_title = db.Column(db.String, unique=True)
	description = db.Column(db.String, unique=True)

	content = db.Column(db.String)
	

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, unique=True)
	email = db.Column(db.String)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String)

	first_name = db.Column(db.String)
	last_name = db.Column(db.String)

	registered_on = db.Column(db.DateTime)


	def __init__(self, username, password, email):
		self.username = username
		self.password = argon2.using(rounds=5).hash(password)
		self.email = email
		self.registered_on = datetime.utcnow()

	def is_authenticated(self):
		return True

	def is_active(self):
		return True
	
	def is_anonymous(self):
		return False
	
	def get_id(self):
		return self.id

	def is_logged_in(self):
		if self.is_authenticated and self.is_authenticated():
			return True
		else:
			return False
	
	def __repr__(self):
		return '<User %r>' % (self.username)

	def verify_password(self, password):
		return argon2.verify(password, self.password)

	def data(self):
		return {
			"username":self.username,
			"email":self.email,
			"password":self.password.split("$")[5],
			"id":self.id,
			"registered_on":self.registered_on,
			"first_name":self.first_name,
			"last_name":self.last_name
		}

class Mail(db.Model):
	id = db.Column(db.Integer, primary_key=True, unique=True)
	timestamp = db.Column(db.DateTime)
	header = db.Column(db.String)
	message = db.Column(db.String)
	status_code = db.Column(db.String)
	error = db.Column(db.String)
	sent_to = db.Column(db.String)
	sent_from = db.Column(db.String)

	def __init__(self, header, message, status_code, error, sent_to, sent_from):
		self.header = header
		self.message = message
		self.status_code = status_code
		self.sent_to = sent_to
		self.sent_from = sent_from
		self.error = error


db.create_all()