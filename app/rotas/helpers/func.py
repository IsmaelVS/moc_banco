# coding: utf-8
"""Arquivo para funções utilizadas no projeto."""

import smtplib
from datetime import datetime

from app.database.tabelas import Conta, Extrato, Usuario, db
from werkzeug.security import check_password_hash


def validar_login(nome, senha):
    """Função de validação dos dados do formulário."""
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    check_pwd = check_password_hash(user.senha, senha)
    if check_pwd:
        return user
    return False


def gerar_uuid(email):
    # user = db.session.query(Usuario).filter_by(
    #     email=email).first()
    data = datetime.now()
    uid = str(data.year)[-2:] + '{:d}'.format(data.month).zfill(2)
    sec = str(data.second)
    hr = str(data.hour)
    # n_id = 1 if 101 > user._id > 1 else 2 if 1001 > user._id > 100 else 3
    idd = '{:d}'.format(0).zfill(10)
    uuid = '{}{}{}{}'.format(uid, idd, hr, sec)

    return uuid


def enviar_token(email, token):
    content = """Token para ativacao da sua conta no banco MOC.\n\n
        Codigo de ativacao: {}\n
        Acesse: http://moc-banco.herokuapp.com/ativar/""".format(token)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('moc.banco@gmail.com', 'mocbanco123')
    mail.sendmail('moc.banco@gmail.com', email, content)


def adic_dinheiro(email, saldo):
    conta = Conta.query.filter_by(email=email).first()
    conta.saldo += saldo
    db.session.commit()
    return conta


def consulta_saldo(email):
    return Conta.query.filter_by(email=email).first()


def checar_email_existente(email):
    return len(Usuario.query.filter_by(email=email).all()) > 0


def tranferir_dinheiro(conta2, valor, email):
    conta = Conta.query.filter_by(email=email).first()
    if conta.saldo >= valor:
        conta.saldo -= valor
        # import ipdb; ipdb.sset_trace()
        conta_dest = Conta.query.filter_by(conta=conta2).first()
        conta_dest.saldo += valor
        # tranferecia_rem = Extrato(email=email, data=datetime.now(), valor=valor)
        # db.session.add(tranferecia_rem)
        # tranferecia_dest = Extrato(data=datetime.now(), valor=valor)
        # db.session.add(tranferecia_dest)
        db.session.commit()
        return True
    return False
