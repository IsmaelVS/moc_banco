# coding: utf-8
"""Arquivo para a criação das tabelas."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db_url = 'sqlite:///db.sqlite'
# db_url = 'postgresql://mocbanco:mocbanco123@localhost:5432/mocbanco_db'
db_url = 'postgres://iyxswvnnweblgs:2ada92bca1b05b697a049be12696312ec6caa0b1452697205abd6ae6aaa3cf04@ec2-54-221-236-144.compute-1.amazonaws.com:5432/dcbj3ac2lobm87'

db = SQLAlchemy()


class Usuario(db.Model):
    """Classe para criação da tabela de usuário no banco."""

    __tablename__ = 'usuario'

    _id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)
    nivel = db.Column(db.Integer, default=0, nullable=False)
    token = db.Column(db.String, default=0, nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return not self.is_authenticated()

    def get_id(self):
        return chr(self._id)

    def __repr__(self):
        return """
        Usuario(nome={}, email={}, status={}, nivel={}, token={})""".format(
            self.nome, self.email, self.status, self.nivel, self.token)


class Conta(db.Model):
    """Classe para criação da tabela de contas no banco."""
    __tablename__ = "conta"

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.relationship('Usuario')
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario._id'))
    saldo = db.Column(db.Float, default=0.0, nullable=False)
    conta = db.Column(db.String, nullable=False)

    def __repr__(self):
        return """Conta(usuario={}, saldo={}, conta={})
        """.format(self.usuario, self.saldo, self.conta)


class Extrato(db.Model):
    """Classe para criação da tabela de extrato no banco."""
    __tablename__ = "extrato"

    id = db.Column(db.Integer, primary_key=True)
    transferencia = db.Column(
        db.Integer, nullable=False, default=1)
    conta = db.relationship('Conta')
    id_conta = db.Column(db.Integer, db.ForeignKey('conta.id'))
    data = db.Column(db.DateTime, nullable=False, default=db.DATETIME)
    valor = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return """Extrato(transferencia={}, email={}, data={}, valor={}
        """.format(self.transferencia, self.email, self.data, self.valor)
