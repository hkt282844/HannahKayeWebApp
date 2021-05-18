import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

def get_db_connection():
  connection = sqlite3.connect('database.db')
  connection.row_factory = sqlite3.Row
  return connection

def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                              (post_id,)).fetchone()
    connection.close()
    if post is None:
      abort(404)
    return post


app = Flask(__name__)

@app.route('/')
def index():
  connection = get_db_connection()
  posts = connection.execute('SELECT * FROM posts').fetchall()
  connection.close()
  return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
  post = get_post(post_id)
  return render_template('post.html', post=post)
