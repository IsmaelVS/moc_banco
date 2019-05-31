"""Arquivo para rota de login."""

from app import Usuario
from app.database.tabelas import Conta
from app.rotas.helpers.func import validar_login
from flask import Blueprint, render_template, request
from flask_login import login_user, logout_user

app = Blueprint('login', __name__)


@app.route('/')
def login_template():
    """Rota para realizar login."""
    logout_user()
    return render_template('login.html')


@app.route('/checar', methods=['POST'])
def check_login():
    """Rota para validar login."""
    result = validar_login(
        request.form.get('nome').lower(), request.form.get('senha'))
    user = Usuario.query.filter_by(
        nome=request.form.get('nome').lower()).first()
    if user:
        if user.status:
            if result:
                conta = Conta.query.filter_by(usuario=user).first()
                login_user(result)
                return render_template(
                    'qr_code.html', token=conta.conta,
                    img='{}.png'.format(conta.conta))
            return render_template('login.html', status=True)
        return render_template('login.html', user=True)
    return render_template('login.html', invalid=True)
