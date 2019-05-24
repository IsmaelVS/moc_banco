from flask import Blueprint, render_template
from flask_login import logout_user

app = Blueprint('menu', __name__)


@app.route('/')
def login_template():
    logout_user()
    return render_template('menu.html')
