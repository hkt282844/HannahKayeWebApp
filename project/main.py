from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from . import db, get_post, get_db_connection
from flask_login import login_required, current_user


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

@main.route('/create', methods=('GET', 'POST'))
@login_required
def create():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      connection = get_db_connection()
      connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
      connection.commit()
      connection.close()
      return redirect(url_for('index'))

  return render_template('create.html')

@main.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
  post = get_post(id)

  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      connection = get_db_connection()
      connection.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
      connection.commit()
      connection.close()
      return redirect(url_for('index'))

  return render_template('edit.html', post=post)

@main.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
  post = get_post(id)
  connection = get_db_connection()
  connection.execute('DELETE FROM posts WHERE id = ?', (id,))
  connection.commit()
  connection.close()
  flash('"{}" was successfully deleted!'.format(post['title']))
  return redirect(url_for('index'))
