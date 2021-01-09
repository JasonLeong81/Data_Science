from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import *
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = 'jason'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # three slashes mean current directory
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login' # for login required
login_manager.login_message_category = 'info'








from Intro import routes
