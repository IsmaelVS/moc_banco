"""Arquivo para realizar deposito na conta."""

from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from app.database.tabelas import Conta
from app.rotas.helpers.func import adic_dinheiro, consulta_saldo

app = Blueprint('adicionar-dinheiro', __name__)


@app.route('/')
@login_required
def adicionar_dinheiro():
    """Rota para adicionar dinheiro."""
    saldo_total = consulta_saldo()
    return render_template('adicionar_dinheiro.html', saldo=saldo_total.saldo)


@app.route('/checar', methods=['POST'])
@login_required
def checar_adicao():
    """Rota para checar adição dinheiro."""
    saldo = request.form.get('saldo')
    conta = adic_dinheiro(float(saldo))
    return render_template(
        'qr_code.html', token=conta.conta,
        img='{}.png'.format(conta.conta))
