import sqlite3
from flask import Flask
from werkzeug.exceptions import abort
from flask_login import LoginManager
from .routes.auth import auth as auth_blueprint
from .routes.main import main as main_blueprint
from .routes.about import about as about_blueprint
from .routes.post import post as post_blueprint
from .routes.link import link as link_blueprint
from .models import db, User

def create_app():
  app = Flask(__name__)

  app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

  db.init_app(app)

  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))

  app.register_blueprint(auth_blueprint)
  app.register_blueprint(main_blueprint)
  app.register_blueprint(about_blueprint)
  app.register_blueprint(post_blueprint)
  app.register_blueprint(link_blueprint)
  return app
