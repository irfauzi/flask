from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask('__name__', template_folder='temperatur/templates', static_folder='temperatur/static')
app.config['SECRET_KEY'] = 'akucinta_iloveu_imissu_kurindu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temperatur.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


    
from temperatur.pengguna.routes import rregister
app.register_blueprint(rregister)
