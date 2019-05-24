# coding: utf-8
"""Arquivo de rota de cadastro."""

from flask import Blueprint, render_template, request
from flask_login import logout_user
from werkzeug.security import generate_password_hash

from app.database.tabelas import Usuario, db
from app.rotas.helpers.func import enviar_token
from app.views.form import FormUsuario, Login
from random import randint

app = Blueprint('cadastro', __name__)


@app.route('/')
def home():
    """Rota inicial, com formulário para cadastro."""
    return render_template('cadastro.html', form=FormUsuario())


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    nome = request.form['nome']
    hashed_senha = generate_password_hash(
        request.form['senha'], method='sha256')
    email = request.form['email']
    # token = randint(10000, 99999)
    user = Usuario(nome=nome, senha=hashed_senha, email=email, token=123)
    enviar_token(request.form['email'], '123')
    db.session.add(user)
    db.session.commit()
    logout_user()
    return render_template('login.html', form=FormUsuario())
