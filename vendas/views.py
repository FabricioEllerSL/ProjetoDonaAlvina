from django.shortcuts import render, redirect
from datetime import datetime
from .models import Venda
from .forms import VendaForm

def display_vendas(request):

    vendas = Venda.objects.all()

    current_date = datetime.now().strftime("%d/%m/%Y")

    context_ = {
        "current_date": current_date,
        "vendas" : vendas
    }

    return render(request, 'vendas/display.html', context_)

def register_venda(request):

    current_date = datetime.now().strftime("%d/%m/%Y")

    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            # Salvar a instância no banco de dados
            form.save()
            return redirect('vendas:display_vendas')  # Redireciona para uma página de sucesso (defina a URL adequada)
    
    form = VendaForm()
    
    context_ = {
        "current_date": current_date,
        "form": form
    }

    return render(request, 'vendas/register.html', context_)
