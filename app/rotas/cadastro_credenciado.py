# coding: utf-8
"""Arquivo de rota de cadastro de credenciado."""

from flask import Blueprint, render_template, request
from flask_login import logout_user

from app.rotas.helpers.forms import FormCadastro
from app.rotas.helpers.func import (checar_usuario_existente, criar_usuario,
                                    enviar_token)

app = Blueprint('cadastro-credenciado', __name__)


@app.route('/')
def home():
    """Rota inicial para cadastro de credenciado."""
    logout_user()
    return render_template('cadastro.html', nivel=1)


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota inicial para checar cadastro de credenciado."""
    form = FormCadastro(request.form)

    if checar_usuario_existente(form.nome.data, form.email.data):
        return render_template('cadastro.html', form=form, email=True), 400
    token = criar_usuario(form.nome.data, form.senha.data, form.email.data, 1)
    if enviar_token(form.email.data, token):
        logout_user()
        return render_template('ativar_cadastro.html', form=form)
    return render_template('cadastro.html', form=form, falha_email=True), 400

    if not form.validate_on_submit():
        return render_template('cadastro.html', form=form)
    return render_template('ativar_cadastro.html')
