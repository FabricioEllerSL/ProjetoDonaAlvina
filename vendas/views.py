from django.shortcuts import render

def display_vendas(request):
    return render(request, 'vendas/display.html')
