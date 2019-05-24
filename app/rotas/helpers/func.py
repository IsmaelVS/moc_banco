"""Arquivo para funções utilizadas no projeto."""

import smtplib
from datetime import datetime

import pyqrcode
from werkzeug.security import check_password_hash

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
    id = '{:d}'.format(user._id).zfill(9)

    return uuid + n_id + id


def gerar_qrcode(uuid):
    code = pyqrcode.create('{}'.format(uuid))
    code.png('{}.png'.format(uuid), scale=6)


def enviar_token(email):
    content = 'Token para ativação da sua conta.'
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('ismael.venturadasilva0@gmail.com', 'password')
    mail.sendmail('ismael.ventiradasilva0@gmail.com',
                  'ismael.venturadasilva0@gmail.com', content)
