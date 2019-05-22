"""Start flask app."""
from flask import Flask
from flask_login import LoginManager

from .tabelas import db, Usuario
from flask_session import Session

login_manager = LoginManager()
session = Session()

app = Flask(__name__, template_folder='templates')


from .login import app as login  # NOQA
app.register_blueprint(login, url_prefix='/login')

from .cadastro import app as cadastro  # NOQA
app.register_blueprint(cadastro, url_prefix='/cadastro')

from .qr_code import app as qr_code  # NOQA
app.register_blueprint(qr_code, url_prefix='/qr-code')


session.init_app(app)
login_manager.init_app(app)
db.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Usuario.query.filter_by(_id=ord(id)).first()
