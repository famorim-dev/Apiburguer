from django.contrib import admin
from .models import Pedidos

@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'status', 'valor_total', 'criacao', 'endereco', 'pagamento')
    list_filter = ('status',)
