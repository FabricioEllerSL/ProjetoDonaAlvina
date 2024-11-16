from django.shortcuts import render
from datetime import datetime
from .models import Venda

def display_vendas(request):

    vendas = Venda.objects.all()

    current_date = datetime.now().strftime("%d/%m/%Y")

    context_ = {
        "current_date": current_date,
        "vendas" : vendas
    }

    return render(request, 'vendas/display.html', context_)
