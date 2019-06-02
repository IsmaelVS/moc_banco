"""Arquivo para realizar transferência."""

from app.database.tabelas import Conta
from app.rotas.helpers.func import (consulta_saldo, tranferir_dinheiro,
                                    validar_conta)
from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

app = Blueprint('transferencia', __name__)


@app.route('/')
@login_required
def transferir_dinheiro():
    """Rota para realizar transferência."""
    return render_template('transferencia.html')


@app.route('/checar', methods=['POST'])
@login_required
def checar_transferencia():
    """Rota para checar transferência."""
    valor = request.form.get('valor')
    conta2 = request.form.get('conta')
    if validar_conta(conta2):
        conta = consulta_saldo()
        if conta2 != conta.conta:
            if tranferir_dinheiro(conta2, float(valor)):
                return render_template(
                    'qr_code.html', token=conta.conta,
                    img='{}.png'.format(conta.conta))
            return render_template('transferencia.html', sem_saldo=True)
        return render_template('transferencia.html', conta=True)
    return render_template('transferencia.html', invalid=True)
