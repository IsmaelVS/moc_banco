# coding: utf-8
"""Arquivo para funções utilizadas no projeto."""

import smtplib
from datetime import datetime

from werkzeug.security import check_password_hash

from app.database.tabelas import Conta, Usuario, db


def validar_login(nome, senha):
    """Função de validação de login de acordo com os dados do formulário.

    Args:
        nome: Nome do usuário.
        senha: Senha do usuário.

    Returns:
        bool: Retorna True se login correto, se não False.
    """
    user = db.session.query(Usuario).filter_by(
        nome=nome).first()
    if user:
        check_pwd = check_password_hash(user.senha, senha)
        if check_pwd:
            return user
        return False


def gerar_uuid(email):
    """Geração de uuid para número da contas

    Args:
        email: email do usuário.

    Returns:
        str: Retorna uma string com o valor do uuid.
    """
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
    """Envio de email com o número do token para ativação da conta.

    Args:
        email: email do usuário.
        token: token para ser enviado.
    """
    content = """Token para ativacao da sua conta no banco MOC.\n\n
        Codigo de ativacao: {}\n
        Acesse: http://moc-banco.herokuapp.com/ativar/""".format(token)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('moc.banco@gmail.com', 'mocbanco123')
    mail.sendmail('moc.banco@gmail.com', email, content)


def adic_dinheiro(email, saldo):
    """Função para realizar deposito na conta.

    Args:
        email: email do usuário.
        saldo: saldo da conta a ser depositado.
    """
    conta = Conta.query.filter_by(email=email).first()
    conta.saldo += saldo
    db.session.commit()
    return conta


def consulta_saldo(email):
    """Função para consultar saldo na conta.

    Args:
        email: email do usuário.

    Returns:
        conta.
    """
    return Conta.query.filter_by(email=email).first()


def checar_email_existente(email):
    """Função para checar se já existe alguma conta com o email digitado.

    Args:
        email: email do usuário.

    Returns:
        int: Quantidade de contas com o email digitado.
    """
    return len(Usuario.query.filter_by(email=email).all()) > 0


def tranferir_dinheiro(conta2, valor, email):
    """Função para checar se já existe alguma conta com o email digitado.

    Args:
        email: email do usuário que deseja realizar a transferência.
        conta2: conta de destino.
        valor: valor da transferência.

    Returns:
        bool: Retorna True se transferência realizada, se não False.
    """
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
