from django.test import TestCase
from rest_framework.test import APITestCase
import json
# Create your tests here.
class TestListagemAgendamentos(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/")
        data =  json.loads(response.content)
        self.assertEqual(data, [])