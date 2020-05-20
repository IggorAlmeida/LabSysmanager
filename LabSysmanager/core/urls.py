from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.client_list, name="clientes"),
    path('pesomedio/', views.peso_medio, name="peso_medio"),

]