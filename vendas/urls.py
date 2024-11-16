from django.urls import path
from . import views

app_name = "vendas"

urlpatterns = [
    path('', views.display_vendas, name='display_vendas'),
    path('register/', views.register_venda, name='register_venda'),
]