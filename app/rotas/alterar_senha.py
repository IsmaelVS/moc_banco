"""Arquivo para alterar senha do usuário."""

from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from app.database.tabelas import db

app = Blueprint('alterar-senha', __name__)


@app.route('/')
@login_required
def atualiza_senha():
    """Rota para alterar senha do usuário."""
    return render_template('alterar_senha.html')


@app.route('/checar', methods=['POST'])
@login_required
def checar_senhas():
    """Rota para validar se senhas são iguais."""
    hashed_senha = generate_password_hash(
        request.form.get('senha'), method='sha256')
    check_pwd = check_password_hash(hashed_senha, request.form.get('c_senha'))
    if check_pwd:
        current_user.senha = hashed_senha
        db.session.commit()
        return render_template('menu.html')
    return render_template('alterar_senha.html', senha=True)
