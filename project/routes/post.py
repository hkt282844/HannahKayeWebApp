from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_required
from ..helper import get_post, create_post, update_post, delete_post

post = Blueprint('post', __name__)

@post.route('/post/<int:post_id>')
def index(post_id):
  current_post = get_post(post_id)
  return render_template('post.html', post=current_post)

@post.route('/post/create', methods=('GET', 'POST'))
@login_required
def create():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      current_post = create_post(title=title, content=content)
      return redirect(url_for('post.index', post_id=current_post.id))

  return render_template('create_post.html')

@post.route('/post/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
  current_post = get_post(id)

  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      update_post(post=current_post, title=title, content=content)
      return redirect(url_for('post.index', post_id=id))

  return render_template('edit_post.html', post=current_post)

@post.route('/post/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
  current_post = get_post(id)
  delete_post(current_post)
  flash('"{}" was successfully deleted!'.format(current_post.title))
  return redirect(url_for('main.index'))
