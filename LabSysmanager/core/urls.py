from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.client_list, name="api"),

]