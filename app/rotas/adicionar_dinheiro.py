from flask import Blueprint, render_template, request
from flask_login import current_user

from app.rotas.helpers.func import adicionar_dinheiro

app = Blueprint('adicionar-dinheiro', __name__)


@app.route('/')
def home():
    """Rota com formulário para validar cadastro."""
    return render_template('adicionar_dinheiro.html')


@app.route('/checar', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    saldo = request.form.get('saldo')
    adicionar_dinheiro(current_user, saldo)
    return render_template('qr_code.html')
