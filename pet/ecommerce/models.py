from django.db import models
import uuid


# Create your models here.
class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.IntegerField


class Endereco(models.Model):

    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=50)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField
    complemento = models.CharField(max_length=100)


class Produto(models.Model):
    nome = models.CharField(max_length=64)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    desconto = models.IntegerField()
    categoria = models.CharField(max_length=32)


class Pedido(models.Model):

    codigo_pedido = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    escolhas_pagamento = [('boleto', 'Boleto'), ('cartao', 'Cartao')]
    tipo_pagamento = models.CharField(
        choices=escolhas_pagamento, max_length=20)
    data_pedido = models.DateTimeField(auto_now_add=True)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    data_entregue = models.DateField(blank=True)


class Rastreamento(models.Model):  # fazer rastreio externamente
    codigo_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    codigo_rastreio = models.CharField(max_length=100)
    data_esperada = models.DateField()


class Carrinho(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)


class Cartao(models.Model):  # validators
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nome_titular = models.CharField(max_length=64)
    numero_cartao = models.IntegerField
    validade_mes = models.IntegerField
    validade_ano = models.IntegerField
