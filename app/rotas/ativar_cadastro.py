from flask import Blueprint, render_template
from app import db
from app.database.tabelas import Conta

app = Blueprint('ativar', __name__)


@app.route('/')
def home():
    """Rota com formulário para validar cadastro."""
    return render_template('ativar_cadastro.html')


@app.route('/checar-ativacao')
def checar_cadastro():
    """Rota para checar cadastro."""
    # Conta.query.filter_by(nome=request.form['email']).first()
    return render_template('qr_code.html')
