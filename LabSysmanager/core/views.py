from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer, ClientLessSerializer


@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        '''
            for tag in ['cidade', 'estado', 'idade_max', 'idade_min']
            if request.query_params.get(tag):
                if tag == 'idade_max':
                    tg_nova = 'idade_lte'
                    params[tg_nova] = request.query_params.get(tag)
                elif tag == 'idade_min':
                    tg_nova = 'idade_gte'
                    params[tg_nova] = request.query_params.get(tag)
                else:
                    params[tag] = request.query_params.get(tag)
        '''
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
