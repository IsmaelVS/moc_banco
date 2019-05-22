"""Arquivo para rota de geração do Qrcode."""

from app.func import gerar_qrcode, gerar_uuid
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, login_user

app = Blueprint('login', __name__)


@app.route('/',  methods=['GET'])
@login_required
def login_template():
    uuid = gerar_uuid()
    gerar_qrcode(uuid=uuid)
    return render_template('qr_code.html', uuid=uuid)
