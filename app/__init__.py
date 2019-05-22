"""Start flask app."""
from flask import Flask
from app.tabelas import db, Usuario
from flask_login import LoginManager
from flask_session import Session

login_manager = LoginManager()
session = Session()

app = Flask(__name__, template_folder='templates')


session.init_app(app)
login_manager.init_app(app)
db.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Usuario.query.filter_by(_id=ord(id)).first()
