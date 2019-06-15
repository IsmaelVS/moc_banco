"""Arquivo para realizar ativação do cadastro."""

from flask import Blueprint, render_template, request
from flask_login import logout_user

from app import db
from app.database.tabelas import Conta, Usuario
from app.rotas.helpers.func import gerar_uuid, verificar_email_e_username
from app.rotas.helpers.forms import FormAtivarCadastro
from app.views.static.gerar_qr_code import gerar_qrcode

app = Blueprint('ativar', __name__)


@app.route('/')
def home():
    """Rota para realizar ativação do cadastro."""
    logout_user()
    form = FormAtivarCadastro()
    return render_template('ativar_cadastro.html', form=form)


@app.route('/checar', methods=['POST'])
def ativar_cadastro():
    """Rota para checar ativação do cadastro."""
    form = FormAtivarCadastro(request.form)
    if not form.validate_on_submit():
        return render_template('ativar_cadastro.html', form=form)
    user = verificar_email_e_username(form.username.data)
    if user:
        if user.status == True:
            return render_template('ativar_cadastro.html', form=form, ativado=True)
        if user.token == form.token.data:
            user.status = True
            n_conta = gerar_uuid(form.username.data)
            conta = Conta(usuario=user, saldo=0.0, conta=n_conta)
            db.session.add(conta)
            db.session.commit()
            gerar_qrcode(n_conta)
            return render_template('login.html')
        return render_template('ativar_cadastro.html', form=form, token=True)
    return render_template('ativar_cadastro.html', form=form, user=True)
