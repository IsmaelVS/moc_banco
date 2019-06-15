from wtforms import PasswordField, SubmitField, TextField
from wtforms.validators import Email, InputRequired, Length

from flask_wtf import FlaskForm


class FormCadastro(FlaskForm):
    nome = TextField('Digite seu nome completo.',
                     validators=[InputRequired()])
    username = TextField('Digite seu username.',
                         validators=[InputRequired()])
    email = TextField('Digite seu email.',
                      validators=[Email(message='Email inválido.'),
                                  InputRequired()])
    senha = PasswordField('Crie uma senha.',
                          validators=[InputRequired(), Length(min=6,
                                      message='Sua senha deve ter no mínimo 6 caracteres.')])
    cadastrar = SubmitField('Cadastrar')


class FormLogin(FlaskForm):
    username = TextField('Digite seu username ou seu email.',
                         validators=[InputRequired()])
    senha = PasswordField('Digite sua senha.',
                          validators=[InputRequired()])
    logar = SubmitField('Logar')


class FormAtivarCadastro(FlaskForm):
    username = TextField('Digite seu username ou seu email.',
                         validators=[InputRequired()])
    token = PasswordField('Digite o número do token recebido.',
                          validators=[InputRequired(), Length(max=5)])
    ativar = SubmitField('Ativar conta')


class FormAdicionarDinheiro(FlaskForm):
    valor = TextField('Digite o valor desejado.',
                      validators=[InputRequired(), Length(max=5)])
    ativar = SubmitField('Ativar conta')


class FormAtivarConta(FlaskForm):
    senha_atual = PasswordField('Digite sua senha atual.',
                                validators=[InputRequired()])
    senha_nova = PasswordField('Digite sua nova senha.',
                               validators=[InputRequired(), Length(min=6)])
    confirmar_senha = PasswordField('Confirme sua nova senha.',
                                    validators=[InputRequired(),
                                                Length(min=6)])
    ativar = SubmitField('Ativar conta')


class FormTransferencia(FlaskForm):
    conta = TextField('Digite o número da conta de destino.',
                      validators=[InputRequired(), Length(max=16)])
    valor = TextField('Digite o valor desejado.',
                      validators=[InputRequired(), Length(max=5)])
    ativar = SubmitField('Ativar conta')
