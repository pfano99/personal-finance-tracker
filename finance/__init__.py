import os, secrets

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
db = SQLAlchemy()
oauth = OAuth(app)

app.config['SECRET_KEY'] = "some key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from finance.main.routes import main
from finance.auth.routes import auth
from finance.user.routes import user
from finance.transaction.routes import transaction
from finance.account.routes import account

app.register_blueprint(main)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(transaction, url_prefix="/transaction")
app.register_blueprint(account, url_prefix="/account")

from finance.models import *
