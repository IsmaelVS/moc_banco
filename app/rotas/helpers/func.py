"""Arquivo para funções utilizadas no projeto."""

import smtplib
from datetime import datetime

import pyqrcode
from werkzeug.security import check_password_hash

from app.database.tabelas import Conta, Usuario, db


def validar_login(nome, senha):
    """Função de validação dos dados do formulário."""
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    check_pwd = check_password_hash(user.senha, senha)
    if check_pwd:
        return user
    return False


def gerar_uuid(nome):
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    data = datetime.now()
    uuid = str(data.year)[-2:] + '{:d}'.format(data.month).zfill(2)
    n_id = 1 if 101 > user._id > 1 else 2 if 1001 > user._id > 100 else 3
    idd = '{:d}'.format(user._id).zfill(9)

    return uuid + n_id + idd


def gerar_qrcode(uuid):
    code = pyqrcode.create('{}'.format(uuid))
    code.png('../../views/static/{}.png'.format(uuid), scale=6)


def enviar_token(email, token):
    content = """Token para ativação da sua conta no banco MOC.\n\n
        Código de ativação: {}\n
        Acesse: http://moc-banco.herokuapp.com/ativar-cadastro""".format(token)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('moc.banco@gmail.com', 'mocbanco123')
    mail.sendmail('moc.banco@gmail.com',
                  email, content)


def adicionar_dinheiro(user, saldo):
    conta = Conta.query.filter_by(usuario=user).first()
    conta.saldo += saldo
    db.add(conta)
    db.commit()
    return conta


def consulta_saldo(user):
    return Conta.query.filter_by(usuario=user).first()
