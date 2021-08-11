from django.contrib import admin
from .models import Produto, Pedido, Rastreamento, Carrinho, Cartao, Cliente, Endereco
# Register your models here.

admin.site.register([Produto, Pedido, Rastreamento,
                     Carrinho, Cartao, Endereco, Cliente])
