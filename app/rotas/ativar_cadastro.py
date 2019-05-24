from flask import render_template

from app import app


@app.route('/ativar-cadastro')
def home():
    """Rota com formulário para validar cadastro."""
    return render_template('ativar_cadastro.html')
