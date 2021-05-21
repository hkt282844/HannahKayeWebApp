from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from . import db, get_post, get_db_connection


main = Blueprint('main', __name__)

@main.route('/')
def index():
  connection = get_db_connection()
  posts = connection.execute('SELECT * FROM posts').fetchall()
  connection.close()
  return render_template('index.html', posts=posts)

@main.route('/<int:post_id>')
def post(post_id):
  post = get_post(post_id)
  return render_template('post.html', post=post)
