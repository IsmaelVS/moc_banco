"""Arquivo para rota de login."""

from flask import Blueprint, redirect, render_template, request, url_for

from flask_login import login_required, login_user

from .form import FormUsuario
from .func import validar_login

app = Blueprint('login', __name__)


@app.route('/',  methods=['GET'])
@login_required
def login_template():
    return render_template('user_index.html')


@app.route('/checar', methods=['POST'])
def check_login():
    """Rota para validar dados do formulário."""
    # import ipdb; ipdb.sset_trace()
    if validar_login(request.form['usuario'], request.form['senha']):
        login_user(True)
        return redirect(url_for('login.login_template'))
    return render_template('login.html', form=FormUsuario(), error=True)
