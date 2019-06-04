# coding: utf-8
"""Arquivo de rota de cadastro."""

from flask import Blueprint, render_template, request
from flask_login import logout_user

from app.database.tabelas import Usuario, db
from app.rotas.helpers.func import (checar_email_existente,
                                    checar_nome_existente, criar_usuario,
                                    enviar_token)

app = Blueprint('cadastro', __name__)


@app.route('/')
def cadastro():
    """Rota inicial para realizar cadastro."""
    logout_user()
    return render_template('cadastro.html', nivel=0)


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    nome = request.form.get('nome', '').lower()
    senha = request.form.get('senha', '')
    email = request.form.get('email', '').lower()
    if nome and senha and email:
        if len(senha) >= 6:
            if checar_email_existente(email):
                return render_template('cadastro.html', email=True), 400
            if checar_nome_existente(nome):
                return render_template('cadastro.html', nome=True), 400
            token = criar_usuario(nome, senha, email, 0)
            if enviar_token(email, token):
                logout_user()
                return render_template('ativar_cadastro.html')
            return render_template('cadastro.html', falha_email=True), 400
        return render_template('cadastro.html', senha=True), 400
    return render_template('cadastro.html', dados=True), 400
