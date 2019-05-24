from flask import render_template

from app import app


@app.route('/ativar-cadastro')
def home():
    """Rota com formulário para validar cadastro."""
    return render_template('ativar_cadastro.html')


@app.route('/checar_ativacao', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    return render_template('qr_code.html')
