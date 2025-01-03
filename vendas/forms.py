from django import forms
from .models import Venda
from . import choices

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['nome_cliente', 'valor_un_kg', 'qtd_kgs', 'descricao_venda', 'metodo_pagamento']
        widgets = {
            'descricao_venda': forms.Textarea(attrs={
                'rows': 4, 
                'cols': 40,
                'class': 'textarea-field',
                }),
            'nome_cliente': forms.TextInput(attrs={
                'class': 'input-field'
            }),
            'valor_un_kg': forms.TextInput(attrs={
                'class': 'input-field'
            }),
            'qtd_kgs': forms.TextInput(attrs={
                'class': 'input-field'
            }),
            'metodo_pagamento': forms.Select(
                attrs={'class': 'choice-field'},
            )
                
        }

class FiltroVendaForm(forms.Form):
    data_inicial = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    data_final = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    metodo_pagamento = forms.ChoiceField(choices=[("", "Todos")] + choices.PAYMENT_METHODS, required=False)