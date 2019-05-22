# coding: utf-8
"""Arquivo para gerar formulários."""

from wtforms import Form, PasswordField, StringField, SubmitField


class FormUsuario(Form):
    """Classe para montar o formulário."""

    nome = StringField('Nome')
    senha = PasswordField('Senha')
    email = StringField('Email')
    btn = SubmitField('Cadastrar')


class Login(Form):
    """Classe para montar o formulário."""

    usuario = StringField('Usuario')
    senha = PasswordField('Senha')
    btn = SubmitField('Logar')
