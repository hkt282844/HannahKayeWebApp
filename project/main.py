from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from . import db
from .helper import get_post, get_all_posts, update_post, delete_post, create_post
from .models import Post
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
  posts = get_all_posts()
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
      create_post(title=title, content=content)
      return redirect(url_for('main.index'))

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
      update_post(post=post, title=title, content=content)
      return redirect(url_for('main.index'))

  return render_template('edit.html', post=post)

@main.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
  post = get_post(id)
  delete_post(post)
  flash('"{}" was successfully deleted!'.format(post.title))
  return redirect(url_for('main.index'))
