from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_login import login_required
from ..helper import get_about, update_about

about = Blueprint('about', __name__)

@about.route('/about')
def index():
  about = get_about()
  return render_template('about.html', about=about)

@about.route('/about/edit', methods=('GET', 'POST'))
@login_required
def edit():
  about = get_about()

  if request.method == 'POST':
    content = request.form['content']
    update_about(about=about, content=content)
    return redirect(url_for('about.index'))

  return render_template('edit_about.html', about=about)
