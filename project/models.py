from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(1000))

class Post(db.Model):
  __tablename__ = "posts"
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)

class About(db.Model):
  __tablename__ = "about"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)

class Link(db.Model):
  __tablename__ = 'links'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  title = db.Column(db.Text, nullable=False)
  content = db.Column(db.Text, nullable=False)
