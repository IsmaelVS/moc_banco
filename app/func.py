"""Arquivo para funções utilizadas no projeto."""

import pyqrcode
from app.tabelas import Usuario, db
from werkzeug.security import check_password_hash


def validar_login(user, senha):
    """Função de validação dos dados do formulário."""
    user = db.session.query(Usuario).filter_by(
        username=user).first()
    return check_password_hash(user.password, senha)


def gerar_uuid():
    uuid = 0
    return uuid


def gerar_qrcode(uuid):
    code = pyqrcode.create('{}'.format(uuid))
    code.png('{}.png'.format(uuid), scale=6)
