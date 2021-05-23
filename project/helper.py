from . import db
from .models import Post, User, About

def get_post(post_id):
  post = Post.query.filter_by(id=post_id).first()
  if post is None:
    abort(404)
  return post

def get_user(email):
  user = User.query.filter_by(email=email).first()
  return user

def get_about():
  about = About.query.filter_by(title='About').first()
  if about is None:
    abort(404)
  return about

def get_all_posts():
  posts = Post.query.all()
  return posts

def update_post(post, title, content):
  post.title = title
  post.content = content
  db.session.commit()

def update_about(about, content):
  about.content = content
  db.session.commit()

def create_post(title, content):
  post = Post(title=title, content=content)
  db.session.add(post)
  db.session.commit()

def delete_post(post):
  db.session.delete(post)
  db.session.commit()
