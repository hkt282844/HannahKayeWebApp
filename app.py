import sqlite3
from flask import Flask, render_template

def get_db_connection():
  connection = sqlite3.connect('database.db')
  connection.row_factory = sqlite3.Row
  return connection

app = Flask(__name__)

@app.route('/')
def index():
  connection = get_db_connection()
  posts = connection.execute('SELECT * FROM posts').fetchall()
  connection.close()
  return render_template('index.html', posts=posts)
