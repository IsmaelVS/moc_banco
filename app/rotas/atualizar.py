"""Arquivo para rota de geração do Qrcode."""

from flask import Blueprint, render_template
from flask_login import current_user

from flask_login import login_required

app = Blueprint('atualizar', __name__)


@app.route('/')
@login_required
def atualiza_usuario():
    return render_template('atualiza.html', usuario=current_user)
