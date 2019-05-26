from app.database.tabelas import Conta
from app.rotas.helpers.func import tranferir_dinheiro
from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

app = Blueprint('transferencia', __name__)


@app.route('/')
@login_required
def transferir_dinheiro():
    """Rota com formulário para validar cadastro."""
    return render_template('transferencia.html')


@app.route('/checar', methods=['POST'])
@login_required
def checar_transferencia():
    """Rota para checar cadastro."""
    valor = request.form.get('valor')
    conta2 = request.form.get('conta')
    email = current_user.email
    conta = Conta.query.filter_by(email=email).first()
    if tranferir_dinheiro(conta2, float(valor), email):
        return render_template(
            'qr_code.html', token=conta.conta,
            img='{}.png'.format(conta.conta))
    return render_template(
        'qr_code.html', token=conta.conta,
        img='{}.png'.format(conta.conta), sem_saldo=True)
