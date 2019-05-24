from flask import Blueprint, render_template

app = Blueprint('ativar', __name__)


@app.route('/')
def home():
    """Rota com formulário para validar cadastro."""
    return render_template('ativar_cadastro.html')


@app.route('/checar_ativacao', methods=['POST'])
def checar_cadastro():
    """Rota para checar cadastro."""
    return render_template('qr_code.html')
