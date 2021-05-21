import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
  app = Flask(__name__)

  app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

  db.init_app(app)

  # blueprint for auth routes in our app
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  # blueprint for non-auth parts of app
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  # blueprint for admin parts of app
  from .admin import admin as admin_blueprint
  app.register_blueprint(admin_blueprint)

  return app

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