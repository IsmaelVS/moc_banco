"""Arquivo para criação do menu."""

from flask import Blueprint, render_template
from flask_login import logout_user

app = Blueprint('menu', __name__)


@app.route('/')
def menu():
    """Rota para o menu."""
    logout_user()
    return render_template('menu.html')
