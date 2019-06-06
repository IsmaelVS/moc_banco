from unittest import TestCase, mock

from flask import url_for

from app import create_app


class TestesCadastro(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app.config['SERVER_NAME'] = 'localhost.test'
        self.app_context = self.app.test_request_context()
        self.client = self.app.test_client()
        self.app_context.push()

    def teste_rota_cadastro(self):
        response = self.client.get(url_for('cadastro.cadastro'))
        self.assertEqual(response.status_code, 200)

    def teste_cadastro_sem_campo_nome(self):
        response = self.client.post(url_for(
            'cadastro.checar_cadastro'),
            data={'senha': '123456', 'email': 'isma@isma.com'})
        self.assertEqual(response.status_code, 400)

    def teste_cadastro_sem_dados(self):
        response = self.client.post(url_for(
            'cadastro.checar_cadastro'),
            data={})
        self.assertEqual(response.status_code, 400)

    def teste_cadastro_com_senha_invalida(self):
        response = self.client.post(url_for(
            'cadastro.checar_cadastro'),
            data={'nome': 'teste', 'senha': '123', 'email': 'teste@teste.com'})
        self.assertEqual(response.status_code, 400)

    @mock.patch('app.rotas.cadastro.enviar_token', return_value=True)
    @mock.patch('app.rotas.cadastro.criar_usuario', return_value='123')
    @mock.patch('app.rotas.cadastro.checar_nome_existente', return_value=False)
    @mock.patch('app.rotas.cadastro.checar_email_existente', return_value=False)
    def teste_cadastro_valido(self, mock_valida_email, mock_valida_nome, mock_criacao_usuario, mock_envio_token):
        response = self.client.post(url_for(
            'cadastro.checar_cadastro'),
            data={'nome': 'teste', 'senha': '123456', 'email': 'teste@teste.com'})
        self.assertEqual(response.status_code, 200)
        mock_envio_token.assert_called_with('teste@teste.com', '123')
