from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("iiec")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'

# ORM
db = SQLAlchemy(app)

class IIEC(db.Model):
	id = db.Column( db.Integer , primary_key = True)
	name    =  db.Column( db.Text )
	age       =  db.Column( db.Integer)
	remarks =  db.Column(db.Text)

# creating Constructor
	def __init__(self , name, age, remarks):

		self.name = name
		self.age = age
		self.remarks = remarks

db.create_all()

ayush = IIEC("ayush" , 10 , "ok")

db.session.add(ayush)
db.session.commit()
