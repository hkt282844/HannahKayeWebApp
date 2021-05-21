from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from . import db, get_post, get_db_connection


admin = Blueprint('admin', __name__)

@admin.route('/admin')
def admin_index():
  connection = get_db_connection()
  posts = connection.execute('SELECT * FROM posts').fetchall()
  connection.close()
  return render_template('admin_index.html', posts=posts)

@admin.route('/create', methods=('GET', 'POST'))
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
      return redirect(url_for('admin_index'))

  return render_template('create.html')

@admin.route('/<int:id>/edit', methods=('GET', 'POST'))
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
      return redirect(url_for('admin_index'))

  return render_template('edit.html', post=post)

@admin.route('/<int:id>/delete', methods=('POST',))
def delete(id):
  post = get_post(id)
  connection = get_db_connection()
  connection.execute('DELETE FROM posts WHERE id = ?', (id,))
  connection.commit()
  connection.close()
  flash('"{}" was successfully deleted!'.format(post['title']))
  return redirect(url_for('admin_index'))
