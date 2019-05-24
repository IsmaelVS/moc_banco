"""Arquivo para rota de login."""

from flask import Blueprint, render_template, request
from flask_login import login_user

from app.rotas.helpers.func import validar_login
from app.views.form import FormUsuario

app = Blueprint('login', __name__)


@app.route('/',  methods=['GET'])
def login_template():
    return render_template('login.html')


@app.route('/checar', methods=['POST'])
def check_login():
    """Rota para validar dados do formulário."""
    # import ipdb; ipdb.sset_trace()
    result = validar_login(request.form['nome'], request.form['senha'])
    if result:
        login_user(result)
        return render_template('qr_code.html')
    return render_template('login.html')
