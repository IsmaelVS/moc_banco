"""Arquivo para realizar deposito na conta."""

from app.database.tabelas import Conta
from app.rotas.helpers.func import adic_dinheiro, consulta_saldo
from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

app = Blueprint('adicionar-dinheiro', __name__)


@app.route('/')
@login_required
def adicionar_dinheiro():
    """Rota para adicionar dinheiro."""
    email = current_user.email
    saldo_total = consulta_saldo(email)
    return render_template('adicionar_dinheiro.html', saldo=saldo_total.saldo)


@app.route('/checar', methods=['POST'])
@login_required
def checar_adicao():
    """Rota para checar adição dinheiro."""
    saldo = request.form.get('saldo')
    email = current_user.email
    conta = Conta.query.filter_by(email=email).first()
    adic_dinheiro(email, float(saldo))
    return render_template(
        'qr_code.html', token=conta.conta,
        img='{}.png'.format(conta.conta))
