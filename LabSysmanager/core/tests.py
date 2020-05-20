from django.test import TestCase
from model_mommy import mommy
from .models import Client


class ModelTests(TestCase):
    def test_client_creation_mommy(self):
        new_client = mommy.make(Client, nome="Iggor Almeida")
        self.assertEqual(new_client.__str__(),"Iggor Almeida")
        self.assertEqual(new_client.__str__(), new_client.nome)

