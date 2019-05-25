from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from app.rotas.helpers.func import adicionar_dinheiro, consulta_saldo

app = Blueprint('adicionar-dinheiro', __name__)


@app.route('/')
@login_required
def adicionar_dinheiro():
    """Rota com formulário para validar cadastro."""
    saldo_total = consulta_saldo(current_user)
    return render_template('adicionar_dinheiro.html', status=saldo_total.saldo)


@app.route('/checar', methods=['POST'])
@login_required
def checar_adicao():
    """Rota para checar cadastro."""
    saldo = request.form.get('saldo')
    result = adicionar_dinheiro(current_user, float(saldo))
    return render_template('qr_code.html', status=result)
