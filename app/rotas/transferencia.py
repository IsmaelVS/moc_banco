"""Arquivo para realizar transferência."""

from app.database.tabelas import Conta, Usuario
from app.rotas.helpers.func import tranferir_dinheiro
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
    user = Usuario.query.filter_by(email=current_user.email)
    conta = Conta.query.filter_by(usuario=user).first()
    if tranferir_dinheiro(conta2, float(valor), email):
        return render_template(
            'qr_code.html', token=conta.conta,
            img='{}.png'.format(conta.conta))
    return render_template(
        'qr_code.html', token=conta.conta,
        img='{}.png'.format(conta.conta), sem_saldo=True)
