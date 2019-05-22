# coding: utf-8
"""Arquivo para gerar formulários."""

from wtforms import Form, PasswordField, StringField, SubmitField


class FormUsuario(Form):
    """Classe para montar o formulário."""

    nome = StringField('Nome')
    senha = PasswordField('Senha')
    email = StringField('Email')
    btn = SubmitField('Logar')
