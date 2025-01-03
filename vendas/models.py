from django.db import models
from . import choices

class Venda(models.Model):
    nome_cliente = models.CharField(max_length=50, blank=True, null=True)
    valor_un_kg = models.DecimalField(max_digits=8, decimal_places=2)
    qtd_kgs = models.DecimalField(max_digits=8, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)
    descricao_venda = models.TextField(default="", blank=True, null=True)
    metodo_pagamento = models.CharField(max_length=10, default=choices.PAYMENT_METHODS[0][0], choices=choices.PAYMENT_METHODS)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        data_formatada = self.data_venda.strftime('%d/%m/%Y')
        return f'Venda | Cliente: {self.nome_cliente if self.nome_cliente else 'Não Informado'}, Data: {data_formatada}'
