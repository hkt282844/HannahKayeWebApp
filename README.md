# HannahKayeWebApp
Simple web app for Hannah Kaye music references

### Prerequisites
* Python3
* Python Environment
* Flask & pacakges: __pip install flask flask-sqlalchemy flask-login__
* SQLite database: create and run __python init_db.py__ to initialize database with an admin user and an initial post and ensure that db.sqlite is placed in **project** directory
* __config.py__ file containing **SECRET_KEY**

### Instructions
1. To start Python environment, run __source env/bin/activate__ from the command line in the root directory.
2. To run the local web app for development, run __export FLASK_APP=project__, then __export FLASK_ENV=development__, then __flask run__ from the command line in the root directory.

### References
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
