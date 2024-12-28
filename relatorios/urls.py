from django.urls import path
from . import views

app_name = "relatorios"

urlpatterns = [
    path('', views.display_relatorios, name='display_relatorios'),
]