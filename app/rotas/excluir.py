from app.database.tabelas import Usuario, db
from flask import Blueprint, render_template
from flask_login import login_required

app = Blueprint('excluir', __name__)


@app.route('/<int:id>')
@login_required
def excluir(id):
    user = Usuario.query.filter_by(_id=id).first()

    db.session.delete(user)
    db.session.commit()

    return render_template('usuarios.html')
