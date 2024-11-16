from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['nome_cliente', 'valor_un_kg', 'qtd_kgs', 'descricao_venda']  # Campos que você quer exibir no formulário
        widgets = {
            'descricao_venda': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Definindo o tamanho do campo de texto
        }
