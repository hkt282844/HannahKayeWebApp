from flask import Flask, Blueprint, render_template
from ..helper import get_all_posts, get_all_links

main = Blueprint('main', __name__)

@main.route('/')
def index():
  posts = get_all_posts()
  links = get_all_links()
  return render_template('index.html', posts=posts, links=links)
