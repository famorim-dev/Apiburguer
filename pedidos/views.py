from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProdutoSerializer

class DataRecebe:
    """
    Recebe a request do front-end.
    """
    @staticmethod
    def receber(request):
        return request.data


class PedidoValida:
    """
    Valida e salva o pedido usando o serializer.
    Retorna um dicionário com sucesso ou erros.
    """
    @staticmethod
    def validar_salvar(dados):
        serializer = ProdutoSerializer(data= dados)
        if serializer.is_valid():
            pedido = serializer.save()
            return {'sucesso': True, 'pedido': pedido}
        return {'sucesso': False, 'erro': serializer.errors}


class RespostaValida:
    """
    Constrói o Response HTTP baseado no resultado do PedidoValida.
    """
    @staticmethod
    def resposta(resultado):
        if resultado['sucesso']:
            return Response({'mensagem': 'Pedido recebido, status pendente' }, status= status.HTTP_200_OK)
        return Response(resultado['erro'], status=status.HTTP_400_BAD_REQUEST)


class CriarPedido(APIView):
    """
    API para criar pedidos.
    Segue o fluxo:
    Pegar dados do front (DataRecebe)
    Validar e salvar (PedidoValida)
    Construir resposta HTTP (RespostaValida)
    """
    def post(self, request):
        dados = DataRecebe.receber(request)
        resultado = PedidoValida.validar_salvar(dados)
        return RespostaValida.resposta(resultado)