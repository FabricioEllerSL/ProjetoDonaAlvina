from django.db import models

class Venda(models.Model):
    nome_cliente = models.CharField(max_length=50)
    valor_un_kg = models.IntegerField()
    qtd_kgs = models.DecimalField(max_digits=8, decimal_places=1)
