from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from .helper import get_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
  email = request.form.get('email')
  password = request.form.get('password')
  remember = True if request.form.get('remember') else False

  user = get_user(email=email)
  if not user or not check_password_hash(user.password, password):
    flash('Please check your login details and try again.')
    return redirect(url_for('auth.login'))

  login_user(user, remember=remember)
  return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))
