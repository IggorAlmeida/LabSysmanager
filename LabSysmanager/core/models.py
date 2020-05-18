from django.db import models


class Client(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    idade = models.PositiveIntegerField()
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=12)
    data_nasc = models.CharField(max_length=10)
    signo = models.CharField(max_length=30)
    mae = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=50)
    cep = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    telefone_fixo = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    altura = models.CharField(max_length=5)
    peso = models.FloatField()
    tipo_sanguineo = models.CharField(max_length=3)
    cor = models.CharField(max_length=30)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.nome