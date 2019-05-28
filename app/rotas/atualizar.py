"""Arquivo para atualizar dados do usuário."""

from flask import Blueprint, render_template
from flask_login import current_user

from flask_login import login_required

app = Blueprint('atualizar', __name__)


@app.route('/')
@login_required
def atualiza_usuario():
    """Rota para atualizar dados do usuário."""
    return render_template('atualiza.html', usuario=current_user)
