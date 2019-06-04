from unittest import TestCase, mock

from flask import url_for

from app import create_app
from app.database.tabelas import Usuario


class Login(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app.config['SERVER_NAME'] = 'localhost.test'
        self.app_context = self.app.test_request_context()
        self.client = self.app.test_client()
        self.app_context.push()

    def teste_status_code_login(self):
        response = self.client.get(url_for('login.login_template'))
        self.assertEqual(response.status_code, 200)

    @mock.patch('app.rotas.login.validar_login', return_value=False)
    def teste_usuario_invalido(self, mock_validar_login):
        response = self.client.post(url_for('login.check_login'))
        self.assertEqual(response.status_code, 400)

    @mock.patch('app.rotas.login.Conta', return_value='ok')
    @mock.patch('app.rotas.login.validar_login', return_value=Usuario(
        _id=1, nome='teste', senha='123456', status=True))
    def teste_login_valido(self, mock_conta, mock_validar_login):
        response = self.client.post(url_for('login.check_login'))
        self.assertEqual(response.status_code, 200)

    @mock.patch('app.rotas.login.Conta', return_value='teste')
    @mock.patch('app.rotas.login.validar_login', return_value=Usuario(
        _id=1, nome='teste', senha='123456', status=False))
    def teste_nao_ativado(self, mock_conta, mock_validar_login):
        response = self.client.post(url_for('login.check_login'))
        self.assertEqual(response.status_code, 400)
