"""Arquivo para rota de login."""

from flask import Blueprint, render_template, request
from flask_login import login_user, logout_user

from app import Usuario
from app.database.tabelas import Conta
from app.rotas.helpers.func import validar_login, pegar_conta
from app.rotas.helpers.forms import FormLogin

app = Blueprint('login', __name__)


@app.route('/')
def login_template():
    """Rota para realizar login."""
    logout_user()
    form = FormLogin()
    return render_template('login.html', form=form)


@app.route('/checar', methods=['POST'])
def check_login():
    """Rota para validar login."""
    form = FormLogin(request.form)

    if not form.validate_on_submit():
        return render_template('login.html', form=form)
    result = validar_login(form.username.data, form.senha.data)
    if result:
        if result.status:
            conta = pegar_conta(result)
            login_user(result)
            return render_template(
                'qr_code.html', token=conta,
                img='{}.png'.format(conta)), 200
        return render_template('login.html', form=form, status=True), 400
    return render_template('login.html', form=form, invalid=True)
