"""Arquivo para rota de login."""

from app.form import FormUsuario
from app.func import validar_login
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, login_user

app = Blueprint('login', __name__)


@app.route('/',  methods=['GET'])
@login_required
def login_template():
    return render_template('user_index.html')


@app.route('/check_login', methods=['POST'])
def check_login():
    """Rota para validar dados do formulário."""
    if validar_login(request.form['nome']):
        login_user(True)
        return redirect(url_for('login.login_template'))
    return render_template('login.html', form=FormUsuario(), error=True)
