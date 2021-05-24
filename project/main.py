from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from . import db
from .helper import *
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
  posts = get_all_posts()
  links = get_all_links()
  return render_template('index.html', posts=posts, links=links)

@main.route('/post/<int:post_id>')
def post(post_id):
  post = get_post(post_id)
  return render_template('post.html', post=post)

@main.route('/about')
def about():
  about = get_about()
  return render_template('about.html', about=about)

@main.route('/post/create', methods=('GET', 'POST'))
@login_required
def create_post():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      create_post_in_db(title=title, content=content)
      return redirect(url_for('main.index'))

  return render_template('create_post.html')

@main.route('/link/create', methods=('GET', 'POST'))
@login_required
def create_link():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      create_link_in_db(title=title, content=content)
      return redirect(url_for('main.index'))

  return render_template('create_link.html')

@main.route('/post/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit_post(id):
  post = get_post(id)

  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      update_post_in_db(post=post, title=title, content=content)
      return redirect(url_for('main.index'))

  return render_template('edit_post.html', post=post)

@main.route('/about/edit', methods=('GET', 'POST'))
@login_required
def edit_about():
  about = get_about()

  if request.method == 'POST':
    content = request.form['content']
    update_about_in_db(about=about, content=content)
    return redirect(url_for('main.about'))

  return render_template('edit_about.html', about=about)

@main.route('/link/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit_link(id):
  link = get_link(id)

  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      update_link_in_db(link=link, title=title, content=content)
      return redirect(url_for('main.index'))

  return render_template('edit_link.html', link=link)

@main.route('/post/<int:id>/delete', methods=('POST',))
@login_required
def delete_post(id):
  post = get_post(id)
  delete_post_from_db(post)
  flash('"{}" was successfully deleted!'.format(post.title))
  return redirect(url_for('main.index'))

@main.route('/link/<int:id>/delete', methods=('POST',))
@login_required
def delete_link(id):
  link = get_link(id)
  delete_link_from_db(link)
  flash('"{}" was successfully deleted!'.format(link.title))
  return redirect(url_for('main.index'))
