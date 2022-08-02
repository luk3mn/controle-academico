from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'plataforma/home.html')

def autenticacao(request):
    return HttpResponse('<h1>Autenticação de Usuários (Login/Cadastro)</h1>')

def sobre(request):
    return render(request, 'plataforma/sobre.html')