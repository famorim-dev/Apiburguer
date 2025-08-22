from .models import Pedidos
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Pedidos.

    Responsável por converter objetos Pedidos em JSON (para enviar ao frontend)
    e também validar e salvar dados recebidos do frontend (POST).

    Todos os campos do modelo Pedidos são incluídos neste serializer.
    """
    class Meta:
        model = Pedidos
        fields = '__all__'