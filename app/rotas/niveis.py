"""Arquivo para escolha do nível do usuário."""

from flask import Blueprint, render_template
from flask_login import logout_user

app = Blueprint('nivel', __name__)


@app.route('/')
def menu():
    """Rota para escolha do nível do usuário."""
    logout_user()
    return render_template('niveis.html')
