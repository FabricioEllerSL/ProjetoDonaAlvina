from datetime import datetime
from django.shortcuts import render

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

