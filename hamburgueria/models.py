from django.db import models

class Status(models.TextChoices):
    """Opções de status de um pedido na hamburgueria."""
    PENDENTE = 'pendente', 'pendente'
    FAZENDO = 'fazendo', 'fazendo'
    ROTA_ENTREGA = 'rota_entrega', 'rota de entrega'
    CONCLUIDO = 'concluido', 'concluido'

class Pagamento(models.TextChoices):
    """Opções de métodos de pagamento disponíveis para o pedido."""
    PIX = 'pix', 'pix'
    CARTAO = 'cartao', 'cartao'
    DINHEIRO = 'dinheiro', 'dinheiro'


class Pedidos(models.Model):
    """
    Model que representa um pedido da hamburgueria.

    Attributes:
        id (AutoField): Identificador único do pedido.
        nome = models.(CharField): nome do cliente.
        email = models.(EmailField) email do cliente.
        itens (JSONField): Lista de produtos e quantidades do pedido.
        valor_total (DecimalField): Valor total do pedido em reais.
        pagamento (CharField): Método de pagamento escolhido.
        endereco (TextField): Endereço de entrega do pedido.
        status (CharField): Status atual do pedido (pendente, fazendo, rota_entrega, concluido).
        criacao (DateTimeField): Data e hora de criação do pedido.
    """
    id = models.AutoField(primary_key= True)
    nome = models.CharField(max_length=100, null= False)
    email = models.EmailField()
    itens = models.JSONField()
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    pagamento = models.CharField(max_length=20, choices= Pagamento.choices)
    endereco = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices)
    criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma string representando o pedido para teste."""
        return f"Pedido {self.id} - {self.status}"
