from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class ClientLessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['nome', 'cpf', 'email', 'senha', 'telefone_fixo', 'celular']
