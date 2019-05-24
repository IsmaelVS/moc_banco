"""Start flask app."""
from flask import Flask
from flask_login import LoginManager

from app.database.tabelas import db, Usuario, db_url
from flask_session import Session

login_manager = LoginManager()
session = Session()


app = Flask(__name__, template_folder='views/templates')


from app.rotas.login import app as login  # NOQA
app.register_blueprint(login, url_prefix='/login')

from app.rotas.cadastro import app as cadastro  # NOQA
app.register_blueprint(cadastro, url_prefix='/cadastro')

from app.rotas.qr_code import app as qr_code  # NOQA
app.register_blueprint(qr_code, url_prefix='/qr-code')

from app.rotas.excluir import app as excluir  # NOQA
app.register_blueprint(excluir, url_prefix='/excluir')

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

session.init_app(app)
login_manager.init_app(app)
db.init_app(app)


@login_manager.user_loader
def load_user(id):
    return Usuario.query.filter_by(_id=ord(id)).first()
