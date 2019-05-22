"""Arquivo para funções utilizadas no projeto."""

from werkzeug.security import check_password_hash

import pyqrcode

from .tabelas import Usuario, db


def validar_login(nome, senha):
    """Função de validação dos dados do formulário."""
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    return check_password_hash(user.senha, senha)


def gerar_uuid():
    uuid = 0
    return uuid


def gerar_qrcode(uuid):
    code = pyqrcode.create('{}'.format(uuid))
    code.png('{}.png'.format(uuid), scale=6)
