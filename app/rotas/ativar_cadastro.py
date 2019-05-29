"""Arquivo para realizar ativação do cadastro."""

from flask import Blueprint, render_template, request
from flask_login import logout_user

from app import db
from app.database.tabelas import Conta, Usuario
from app.rotas.helpers.func import gerar_uuid
from app.views.static.gerar_qr_code import gerar_qrcode

app = Blueprint('ativar', __name__)


@app.route('/')
def home():
    """Rota para realizar ativação do cadastro."""
    logout_user()
    return render_template('ativar_cadastro.html')


@app.route('/checar', methods=['POST'])
def ativar_cadastro():
    """Rota para checar ativação do cadastro."""
    token = request.form.get('token')
    email = request.form.get('email')
    user = Usuario.query.filter_by(email=email).first()
    if user:
        if user.token == token:
            user.status = True
            n_conta = gerar_uuid(email)
            conta = Conta(email=email, saldo=0.0, conta=n_conta)
            db.session.add(conta)
            db.session.commit()
            gerar_qrcode(n_conta)
            return render_template('login.html')
        return render_template('ativar_cadastro.html', token=True)
    return render_template('ativar_cadastro.html', user=True, token=False)
