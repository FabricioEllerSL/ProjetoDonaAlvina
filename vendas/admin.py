from django.contrib import admin
from .models import Venda

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('nome_cliente', 'valor_un_kg', 'qtd_kgs')
