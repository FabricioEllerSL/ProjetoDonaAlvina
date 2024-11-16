from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('navegacao/', views.navigation_page, name='navigation_page'),
]