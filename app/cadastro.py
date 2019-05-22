# coding: utf-8
"""Arquivo de rota de cadastro."""

from flask import Blueprint, render_template
from flask_login import logout_user
from form import FormUsuario

app = Blueprint('cadastro', __name__)


@app.route('/')
def home():
    """Rota inicial, com formulário para cadastro."""
    logout_user()
    return render_template('cadastro.html', form=FormUsuario())
