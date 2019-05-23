# coding: utf-8
"""Projeto web utilizando Flask e Flask-login."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'teste'

# db_url = 'sqlite:///db.sqlite'
db_url = 'postgres://pvgugjjzwjvpil:9c7adefda7aa2f5a678de9db6b484c82d37e2c88e5d77d8525315934cb9dc974@ec2-23-21-129-125.compute-1.amazonaws.com:5432/d3kvra84jha1nf'

db = SQLAlchemy()


class Usuario(db.Model):
    """Classe para criação da tabela usuário no banco."""

    __tablename__ = 'usuario'

    _id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    nivel = db.Column(db.Integer, default=0, nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return not self.is_authenticated()

    def get_id(self):
        return chr(self._id)

    def __init__(self, nome, senha, email, nivel):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.nivel = nivel

    def __repr__(self):
        return """
        Usuario(nome={}, senha={}, nivel={})""".format(
            self.nome, self.senha, self.nivel)


class Conta(db.Model):
    __tablename__ = "conta"

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario._id'))
    id_extrato = db.Column(db.Integer, db.ForeignKey('extrato.id'))
    usuario = db.relationship('Usuario')
    extrato = db.relationship('Extrato')
    conta = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return """Conta(usuario={}, extrato={}, conta={}, status={})
        """.format(self.usuario, self.extrato, self.conta, self.status)


class Extrato(db.Model):
    __tablename__ = "extrato"

    id = db.Column(db.Integer, primary_key=True)
    transferencia = db.Column(
        db.String(300), nullable=False, default="Transferência")
    data = db.Column(db.DateTime, nullable=False, default=db.DATETIME)
    valor = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return """Extrato(transferencia={}, data={}, valor={}
        """.format(self.transferencia, self.data, self.valor)
