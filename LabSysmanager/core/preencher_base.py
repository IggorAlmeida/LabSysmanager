import json
import io
from .serializers import ClientSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def populate():
    json_file = open('../clientes.json', 'r')
    dados = json.load(json_file)
    for obj in dados:
        serializer = ClientSerializer(obj)
        content = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()


if __name__ == "__main__":
    populate()

