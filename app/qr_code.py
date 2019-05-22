"""Arquivo para rota de geração do Qrcode."""

from flask import Blueprint, render_template

from flask_login import login_required

from .func import gerar_qrcode, gerar_uuid

app = Blueprint('qr_code', __name__)


@app.route('/',  methods=['GET'])
@login_required
def login_template():
    uuid = gerar_uuid()
    gerar_qrcode(uuid=uuid)
    return render_template('qr_code.html', uuid=uuid)
