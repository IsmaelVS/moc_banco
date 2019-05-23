"""Arquivo para funções utilizadas no projeto."""

from datetime import datetime

from werkzeug.security import check_password_hash

import pyqrcode
from app.database.tabelas import Usuario, db


def validar_login(nome, senha):
    """Função de validação dos dados do formulário."""
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    return check_password_hash(user.senha, senha)


def gerar_uuid(nome):
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    data = datetime.now()
    uuid = str(data.year)[-2:] + '{:d}'.format(data.month).zfill(2)
    n_id = 1 if 101 > user._id > 1 else 2 if 1001 > user._id > 100 else 3

    return uuid + n_id


def gerar_qrcode(uuid):
    code = pyqrcode.create('{}'.format(uuid))
    code.png('{}.png'.format(uuid), scale=6)
