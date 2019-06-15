# coding: utf-8
"""Arquivo para funções utilizadas no projeto."""

import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

from werkzeug.security import check_password_hash, generate_password_hash

from app.database.tabelas import Conta, Extrato, Usuario, db
from flask_login import current_user


def validar_login(username, senha):
    """Função de validação de login de acordo com os dados do formulário.

    Args:
        username: Username ou email do usuário.
        senha: Senha do usuário.

    Returns:
        bool: Retorna instância do banco se login correto, se não False.
    """
    user_username = db.session.query(Usuario).filter_by(
        username=username.lower()).first()
    user_email = db.session.query(Usuario).filter_by(
        email=username).first()

    if user_username:
        return user_username if check_password_hash(
            user_username.senha, senha) else False
    elif user_email:
        return user_email if check_password_hash(
            user_email.senha, senha) else False
    return False

def verificar_email_e_username(username):
    """Função verificar se email ou username digitado é válido.

    Args:
        username: Username ou email do usuário.

    Returns:
        bool: Retorna instância do banco se login correto, se não False.
    """
    user_username = db.session.query(Usuario).filter_by(
        username=username.lower()).first()
    user_email = db.session.query(Usuario).filter_by(
        email=username).first()

    if user_username:
        return user_username
    elif user_email:
        return user_email
    return False


def gerar_uuid(email):
    """Geração de uuid para número da contas

    Args:
        email: Email do usuário.

    Returns:
        str: Retorna uma string com o valor do uuid.
    """
    user = Usuario.query.filter_by(email=email).first()
    data = datetime.now()
    primeiro = str(data.year)[-2:] + '{:d}'.format(data.month).zfill(2)
    segundo = 1 if 101 > user._id > 1 else 2 if 1001 > user._id > 100 else 3
    terceiro = '{:d}'.format(user._id).zfill(9)
    dig1 = str(int(primeiro[0]) + int(primeiro[1]) +
               int(primeiro[2]) + int(primeiro[3]))[0]
    dig2 = str(int(terceiro[0]) + int(terceiro[1]) + int(terceiro[2]) +
               int(terceiro[3]) + int(terceiro[4]) + int(terceiro[5]) +
               int(terceiro[6]) + int(terceiro[7]) + int(terceiro[8]))[0]
    uuid = '{}{}{}{}{}'.format(primeiro, segundo, terceiro, dig1, dig2)

    return uuid


def enviar_token(email, token):
    """Envio de email com o número do token para ativação da conta.

    Args:
        email: email do usuário.
        token: token para ser enviado.
    """
    message = """Token para ativacao da sua conta no banco MOC.\n
        Codigo de ativacao: {}\n
        Acesse: http://moc-banco.herokuapp.com/ativar/""".format(token)
    try:
        msg = MIMEMultipart()

        password = 'mocbanco123'
        msg['From'] = 'moc.banco@gmail.com'
        msg['To'] = email
        msg['Subject'] = "Token para ativação da conta"
        msg.attach(MIMEText(message))

        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        return True
    except Exception:
        return False


def adic_dinheiro(saldo):
    """Função para realizar deposito na conta.

    Args:
        saldo: saldo da conta a ser depositado.
    """
    conta = consulta_saldo()
    conta.saldo += saldo
    db.session.commit()
    return conta


def pegar_conta(usuario):
    """Função para pegar numero da conta.

    Returns:
        conta.
    """
    return Conta.query.filter_by(usuario=usuario).first().conta


def criar_usuario(nome, username, senha, email, nivel):
    """Função para criação de usuário."""
    token = randint(10000, 99999)
    hashed_senha = generate_password_hash(senha, method='sha256')
    user = Usuario(nome=nome, username=username.lower(), senha=hashed_senha,
                   email=email, token=token, nivel=nivel)
    db.session.add(user)
    db.session.commit()
    return token


def consulta_saldo():
    """Função para consultar saldo na conta.

    Returns:
        conta.
    """
    return Conta.query.filter_by(usuario=current_user).first()


def checar_usuario_existente(nome, email):
    """Função para checar se já existe alguma conta com o email digitado.

    Args:
        nome: nome do usuário.
        email: email do usuário.

    Returns:
        int: Quantidade de contas com o email digitado.
    """
    return len(Usuario.query.filter_by(email=email).all()) > 0 or\
        len(Usuario.query.filter_by(nome=nome).all()) > 0


def tranferir_dinheiro(conta2, valor):
    """Função para checar se já existe alguma conta com o email digitado.

    Args:
        conta2: conta de destino.
        valor: valor da transferência.

    Returns:
        bool: Retorna True se transferência realizada, se não False.
    """
    conta = consulta_saldo()
    if conta.saldo >= valor and valor > 0:
        data_transferencia = datetime.now()
        conta.saldo -= valor
        conta_dest = Conta.query.filter_by(conta=conta2).first()
        conta_dest.saldo += valor
        tranferecia_rem = Extrato(transferencia=0, conta=conta,
                                  valor=valor, data=data_transferencia)
        db.session.add(tranferecia_rem)
        tranferecia_dest = Extrato(transferencia=1, conta=conta_dest,
                                   valor=valor, data=data_transferencia)
        db.session.add(tranferecia_dest)
        db.session.commit()
        return True
    return False


def validar_conta(num_cont):
    """Função para validar se número de conta digitada é valida."""
    conta = Conta.query.filter_by(conta=num_cont).first()
    if conta:
        return True
    return False
