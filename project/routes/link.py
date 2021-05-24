from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_required
from ..helper import get_link, create_link, update_link, delete_link

link = Blueprint('link', __name__)

@link.route('/link/create', methods=('GET', 'POST'))
@login_required
def create():
  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      create_link(title=title, content=content)
      return redirect(url_for('main.index'))

  return render_template('create_link.html')

@link.route('/link/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
  current_link = get_link(id)

  if request.method == 'POST':
    title = request.form['title']
    content = request.form['content']

    if not title:
      flash('Title is required!')
    else:
      update_link(link=current_link, title=title, content=content)
      return redirect(url_for('main.index'))

  return render_template('edit_link.html', link=current_link)

@link.route('/link/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
  current_link = get_link(id)
  delete_link(current_link)
  flash('"{}" was successfully deleted!'.format(current_link.title))
  return redirect(url_for('main.index'))
