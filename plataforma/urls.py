from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='plataforma.home'),
    path('autenticacao/', views.autenticacao, name='plataforma.autenticacao'),
    path('sobre/', views.sobre, name='plataforma.sobre'),
]