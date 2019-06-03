from unittest import TestCase, mock

from flask import url_for

from app import create_app


class Login(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app.config['SERVER_NAME'] = 'localhost.test'
        self.app_context = self.app.test_request_context()
        self.client = self.app.test_client()
        self.app_context.push()

    @mock.patch('app.rotas.login.validar_login', return_value=False)
    def teste(self, mock_validar_login):
        response = self.client.post(url_for('login.check_login'),
                                    data={'nome': 'teste'})
        self.assertEqual(response.status_code, 400)

    def teste_status_code_login(self):
        response = self.client.get(url_for('login.login_template'))
        self.assertEqual(response.status_code, 200)
