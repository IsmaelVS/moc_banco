# coding: utf-8
"""Arquivo de rota de cadastro de credenciado."""

from random import randint

from app.database.tabelas import Usuario, db
from app.rotas.helpers.func import checar_email_existente, enviar_token
from flask import Blueprint, render_template, request
from flask_login import logout_user
from werkzeug.security import generate_password_hash

app = Blueprint('cadastro-credenciado', __name__)


@app.route('/')
def home():
    """Rota inicial para cadastro de credenciado."""
    logout_user()
    return render_template('cadastro.html', nivel=1)


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota inicial para checar cadastro de credenciado."""
    nome = request.form.get('nome').lower()
    hashed_senha = generate_password_hash(
        request.form.get('senha'), method='sha256')
    email = request.form.get('email')
    token = randint(10000, 99999)
    if checar_email_existente(email):
        return render_template('cadastro.html', user=True)
    user = Usuario(nome=nome, senha=hashed_senha,
                   email=email, token=token, nivel=1)
    enviar_token(email, token)
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template('ativar_cadastro.html')
