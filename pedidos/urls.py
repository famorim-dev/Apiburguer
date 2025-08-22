from django.urls import path
from .views import CriarPedido

urlpatterns = [
    path('pedidos/', CriarPedido.as_view(), name='criar-pedido'),
]