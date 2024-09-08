from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define a rota principal para a função 'index'
]
