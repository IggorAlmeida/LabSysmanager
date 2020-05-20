from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer, ClientLessSerializer


@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        params = {}
        list_tags = ['cidade', 'estado', 'idade_max', 'idade_min']
        for tag in list_tags:
            if request.query_params.get(tag):
                if tag == 'idade_max':
                    tg_nova = 'idade__lte'
                    params[tg_nova] = request.query_params.get(tag)
                elif tag == 'idade_min':
                    tg_nova = 'idade__gte'
                    params[tg_nova] = request.query_params.get(tag)
                else:
                    params[tag] = request.query_params.get(tag)

        clients = Client.objects.filter(**params)
        serializer = ClientLessSerializer(clients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def peso_medio(request):
    if request.method == 'GET':
        params = {}
        list_tags = ['cidade', 'estado', 'idade_max', 'idade_min']
        for tag in list_tags:
            if request.query_params.get(tag):
                if tag == 'idade_max':
                    tg_nova = 'idade__lte'
                    params[tg_nova] = request.query_params.get(tag)
                elif tag == 'idade_min':
                    tg_nova = 'idade__gte'
                    params[tg_nova] = request.query_params.get(tag)
                else:
                    params[tag] = request.query_params.get(tag)

        clients = Client.objects.filter(**params)
        total = {}
        total['quantidade_clientes'] = len(clients)

        if len(clients) > 0:
            total['peso'] = 0
            for x in range(len(clients)):
                total['peso'] += clients[x].peso
            total['peso_medio'] = round(float(total['peso']/total['quantidade_clientes']),3)
        else:
            total['peso']=0
            total['quantidade_clientes'] = None

        return Response(total)