import io
import json
import requests
from celery import shared_task
from .serializers import ClientSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def populate_task():
    json_file = open('/opt/integracao/lab/clientes.json', 'r')
    dados = json.load(json_file)
    for obj in dados:

        cep = obj.get('cep')
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        stream = io.BytesIO(response.content)
        data = JSONParser().parse(stream)

        obj['cidade'] = data.get('localidade')
        obj['estado'] = data.get('uf')
        '''
        serializer = ClientSerializer(obj)
        content = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        '''
        serializer = ClientSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()