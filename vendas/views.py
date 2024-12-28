from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from .models import Venda
from .forms import VendaForm, FiltroVendaForm
from django.db.models import Q

def display_vendas(request):

    vendas = Venda.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        vendas = vendas.filter(
        Q(nome_cliente__istartswith=search_query) |
        Q(data_venda__icontains=search_query)
    )

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

            form.save()
            return redirect('vendas:display_vendas')
    
    form = VendaForm()
    
    context_ = {
        "current_date": current_date,
        "form": form
    }

    return render(request, 'vendas/register.html', context_)

def update_venda(request, id):

    current_date = datetime.now().strftime("%d/%m/%Y")

    venda = get_object_or_404(Venda, id=id)

    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():

            form.save()
            return redirect('vendas:display_vendas')
    
    form = VendaForm(instance=venda)
    
    context_ = {
        "current_date": current_date,
        "form": form
    }

    return render(request, 'vendas/register.html', context_)


def delete_venda(request, id):

    venda = get_object_or_404(Venda, id=id)

    venda.delete()
    return redirect('vendas:display_vendas')
    
    
def display_relatorios(request):
    vendas = Venda.objects.all() 
    form = FiltroVendaForm(request.GET or None)

    if form.is_valid():

        data_inicial = form.cleaned_data.get('data_inicial')
        data_final = form.cleaned_data.get('data_final')
        metodo_pagamento = form.cleaned_data.get('metodo_pagamento')

        if data_inicial:
            vendas = vendas.filter(data_venda__gte=data_inicial)
        if data_final:
            data_final = datetime.combine(data_final, datetime.max.time())
            vendas = vendas.filter(data_venda__lte=data_final)
        if metodo_pagamento:
            print(metodo_pagamento)
            vendas = vendas.filter(metodo_pagamento=metodo_pagamento)

    somatorio_vendas = 0.0

    for venda in vendas:

        somatorio_vendas += float(venda.valor_total)

    context_ = {
        'vendas': vendas,
        'form': form,
        'somatorio': f"{float(somatorio_vendas):,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
    }

    return render(request, 'vendas/relatorios.html', context=context_)