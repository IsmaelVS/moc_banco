"""Arquivo para funções utilizadas no projeto."""

from datetime import datetime

import pyqrcode
from werkzeug.security import check_password_hash

from .tabelas import Usuario, db


def validar_login(nome, senha):
    """Função de validação dos dados do formulário."""
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    return check_password_hash(user.senha, senha)


def gerar_uuid():
    data = datetime.now()
    uuid = str(data.year)[-2:] + '{:d}'.format(data.month).zfill(2)

    return uuid


def gerar_qrcode(uuid):
    code = pyqrcode.create('{}'.format(uuid))
    code.png('{}.png'.format(uuid), scale=6)
