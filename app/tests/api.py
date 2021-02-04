from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Cidades, Demandas


class ApiTests(APITestCase):
    def setUp(self):
        self.username = 'bsgabrielsilva'
        self.email = 'bsgabrielsilva@outlook.com'
        self.password = '123Mudar'
        self.cidade = Cidades.objects.create(cidade='Macapá', slug='macapa', estado='Amapá')
        self.api_registro()
        self.api_login()

    def api_registro(self):
        url = reverse('registro-list')
        data = {'username': self.username, 'email': self.email, 'password': self.password}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def api_login(self):
        url = reverse('api-root')
        url_login = f'{url}login/'
        data = {'username': self.username, 'password': self.password}
        response = self.client.post(url_login, data, format='json')
        if response.status_code == status.HTTP_200_OK:
            self.client.credentials(HTTP_AUTHORIZATION=f"Token {response.json()['token']}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def criar_demanda(self):
        user = User.objects.get(username=self.username)
        Demandas.objects.create(descricao="Peça do Câmbio Manual 5", logradouro="Avenida dos Motos, Nº 1121",
                                complemento="Em frente a Honda", bairro="Escola Da vida", cep="00.100-221",
                                cidade=self.cidade, email="bsgabrielsilva@outlook.com", telefone="(00) 3300-2201",
                                celular="(00) 0 3333-0001", user=user)

    def test_listar_cidades(self):
        url = reverse('cidades-list')
        cidade = "Macapá"
        query = f"?cidade={cidade}"
        response = self.client.get(f'{url}{query}', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(int(response.json()['count']), Cidades.objects.count())

    def test_cadastro_demanda(self):
        url = reverse('demandas-list')
        data = {"descricao": "Peça do Câmbio Manual 5", "logradouro": "Avenida dos Motos, Nº 1121",
                "complemento": "Em frente a Honda", "bairro": "Escola Da vida",
                "cep": "00.100-221", "cidade": self.cidade.slug, "email": "bsgabrielsilva@outlook.com",
                "telefone": "(00) 3300-2201", "celular": "(00) 0 3333-0001"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_editar_demanda(self):
        self.criar_demanda()
        url = reverse('demandas-list')
        data = {"descricao": "Peça do Câmbio Manual 4", "logradouro": "Avenida dos Motos, Nº 1121",
                "complemento": "Em frente a Honda", "bairro": "Escola",
                "cep": "00.100-221", "cidade": self.cidade.slug, "email": "bsgabrielsilva@outlook.com",
                "telefone": "(00) 3300-2201", "celular": "(00) 0 3333-0001"}
        response = self.client.put(f'{url}1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['descricao'], data['descricao'])
        self.assertEqual(response.json()['bairro'], data['bairro'])

    def test_finalizar_demanda(self):
        self.criar_demanda()
        url = reverse('finalizar_demanda-list')
        data = {'status': 'Finalizada'}
        response = self.client.put(f"{url}1/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_206_PARTIAL_CONTENT)
        self.assertEqual(response.json()['status'], data['status'])

    def test_list_demandas(self):
        self.criar_demanda()
        url = reverse('demandas-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(int(response.json()['count']), Demandas.objects.count())

    def test_remover_demanda(self):
        self.criar_demanda()
        url = reverse('demandas-list')
        response = self.client.delete(f"{url}1/", format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
