# coding: utf-8
"""Arquivo de rota de cadastro."""

from flask import Blueprint, render_template, request
from flask_login import logout_user

from app.rotas.helpers.forms import FormCadastro
from app.rotas.helpers.func import (checar_usuario_existente, criar_usuario,
                                    enviar_token)

app = Blueprint('cadastro', __name__)


@app.route('/')
def cadastro():
    """Rota inicial para realizar cadastro."""
    logout_user()
    form = FormCadastro()
    return render_template('cadastro.html', form=form, nivel=0)


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    form = FormCadastro(request.form)

    if not form.validate_on_submit():
        return render_template('cadastro.html', form=form)
    if checar_usuario_existente(form.nome.data, form.email.data):
        return render_template('cadastro.html', form=form, email=True), 400
    token = criar_usuario(form.nome.data, form.username.data, form.senha.data, form.email.data, 0)
    if enviar_token(form.email.data, token):
        logout_user()
        return render_template('ativar_cadastro.html', form=form)
    return render_template('cadastro.html', form=form, falha_email=True), 400
