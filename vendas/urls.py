from django.urls import path
from . import views

app_name = "vendas"

urlpatterns = [
    path('', views.display_vendas, name='display_vendas'),
    path('register/', views.register_venda, name='register_venda'),
    path('update/<int:id>', views.update_venda, name='update_venda'),
    path('delete/<int:id>', views.delete_venda, name='delete_venda'),
]