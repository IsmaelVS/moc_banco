# coding: utf-8
"""Arquivo de rota de cadastro."""

from random import randint

from flask import Blueprint, render_template, request
from flask_login import logout_user
from werkzeug.security import generate_password_hash

from app.database.tabelas import Usuario, db
from app.rotas.helpers.func import checar_email_existente, enviar_token

app = Blueprint('cadastro', __name__)


@app.route('/')
def home():
    """Rota inicial, com formulário para cadastro."""
    logout_user()
    return render_template('cadastro.html')


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    nome = request.form['nome']
    hashed_senha = generate_password_hash(
        request.form['senha'], method='sha256')
    email = request.form['email']
    token = randint(10000, 99999)
    if checar_email_existente(email):
        return render_template('cadastro.html', user=True)
    user = Usuario(nome=nome, senha=hashed_senha, email=email, token=token)
    enviar_token(email, token)
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template('ativar_cadastro.html')
