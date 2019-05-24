from app import app
from flask import render_template
from flask_login import login_user


@app.route('/',  methods=['GET'])
def login_template():
    login_user()
    return render_template('menu.html')
