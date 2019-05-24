from flask import render_template
from flask_login import login_user

from app import app


@app.route('/')
def login_template():
    login_user()
    return render_template('menu.html')
