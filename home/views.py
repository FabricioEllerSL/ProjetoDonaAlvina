from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

def landing_page(request):

    """
        This view returns the first page of the application
    """

    current_date = datetime.now().strftime("%d/%m/%Y")

    context_ = {
        "current_date": current_date
    }

    return render(request, 'home/landing.html', context_)

def navigation_page(request):
    """
        This view returns the navigation page, where you can
        manage the CRUDs
    """
    current_date = datetime.now().strftime("%d/%m/%Y")

    context_ = {
        "current_date": current_date
    }

    return render(request, 'home/navigation.html', context_)

# LOGIN SECTION

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('home:navigation_page')  # Substitua 'home' pela URL desejada
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'home/login.html', {'form': form})


