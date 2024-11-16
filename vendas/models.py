from django.db import models

class Venda(models.Model):
    nome_cliente = models.CharField(max_length=50, blank=True, null=True)
    valor_un_kg = models.IntegerField()
    qtd_kgs = models.DecimalField(max_digits=8, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)
    descricao_venda = models.TextField(default="", blank=True, null=True)

    def __str__(self):
        valor_total = self.valor_un_kg * self.qtd_kgs
        data_formatada = self.data_venda.strftime('%d/%m/%Y')
        return f'Venda | Cliente: {self.nome_cliente}, Data: {data_formatada} Valor: R${str(valor_total).replace('.', ',')}'
