# Lassysmanager
   
O projeto tem por objetivo disponibilizar uma api para consulta de dados referentes aos clientes do plano. Dados são lidos, completados e tratados.

Requisitos e Bancos
Python = 3.6.9
MySQL = 5.7.3
Redis = 5.0.8

## Installing / Getting started

1) git clone https://github.com/IggorAlmeida/LabSysmanager.git
2) cd to the directory where requirements.txt is located.
3) activate your virtualenv.
4) run: pip install -r requirements.txt in your shel


## Running / Getting started

Agora para rodar a aplicação cada um dos comandos deve ser executado em um terminal diferente (mas usando o mesmo virtual enviroment)

terminal1: projeto_sys_manager/LabSysmanager/
```shell
redis-server
```
terminal2:projeto_sys_manager/LabSysmanager/
```shell
celery -A LabSysmanager worker --loglevel=info
```

terminal3:projeto_sys_manager/LabSysmanager
```shell
celery -A LabSysmanager beat
```

terminal4:projeto_sys_manager/LabSysmanager
```shell
python manage.py runserver
```

## API

Dois endpoints foram criados, ambos com filtros.

endpoints:

1) Listar todos os clientes (com filtros)

a) Lista todos os clientes

http://localhost:8000/clientes/

b) Lista todos os clientes filtrados pelos parâmetros enviados (idade_max, idade_min, cidade, estado)

http://localhost:8000/clientes/?cidade=Rio de Janeiro&&idade_max=50&&estado=RJ&&idade_min=30

2) Listar o peso médio dos clientes (com filtros)

a) Lista todos os clientes

http://localhost:8000/pesomedio/

b) Lista o peso médio dos clientes filtrados pelos parâmetros enviados (idade_max, idade_min, cidade, estado)

http://localhost:8000/pesomedio/?cidade=Rio de Janeiro&&idade_max=50&&estado=RJ&&idade_min=30
