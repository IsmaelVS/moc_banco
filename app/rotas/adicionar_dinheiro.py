from flask import Blueprint, render_template, request
from flask_login import current_user

from app.rotas.helpers.func import adicionar_dinheiro, consulta_saldo

app = Blueprint('adicionar-dinheiro', __name__)


@app.route('/')
def home():
    """Rota com formulário para validar cadastro."""
    saldo = consulta_saldo(current_user)
    return render_template('adicionar_dinheiro.html', status=saldo.saldo)


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    saldo = request.form.get('saldo')
    result = adicionar_dinheiro(current_user, saldo)
    return render_template('qr_code.html', status=result.saldo)
