from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# APP CONFIG
app = Flask(__name__)

app.config['SECRET_KEY'] = '582b482752caf974aa4ab020395f993a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from main import views
