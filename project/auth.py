from flask import Flask, Blueprint, render_template, request, url_for, flash, redirect
from . import db, get_post, get_db_connection

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
  return render_template('login.html')

@auth.route('/logout')
def logout():
  return 'Logout'
