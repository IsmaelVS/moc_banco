"""Arquivo para rota de geração do Qrcode."""

# from app.rotas.helpers.func import gerar_uuid
from flask import Blueprint, render_template
from flask_login import login_required

app = Blueprint('qr-code', __name__)


@app.route('/',  methods=['GET'])
@login_required
def login_template():
    """Rota para o Qrcode."""
    # uuid = gerar_uuid(request.form['usuario'])
    # gerar_qrcode(uuid)
    return render_template('qr_code.html')
