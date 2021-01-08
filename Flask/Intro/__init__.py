from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = 'jason'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # three slashes mean current directory

db = SQLAlchemy(app)

from Intro import routes
