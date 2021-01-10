from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import *
from flask_login import LoginManager
from flask_mail import Mail
import os # for environmental variable

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jason'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # three slashes mean current directory
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login' # for login required
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'leongjason822@gmail.com' # what we use to send emails
app.config['MAIL_PASSWORD'] = '378100Yc'
mail = Mail(app)






from Intro import routes
