from django.shortcuts import render
from django.http import HttpResponse
from plataforma.models import Curso

def home(request):
    curso = Curso.objects.all()
    return render(request, 'plataforma/home.html', {'cursos':curso})

def autenticacao(request):
    return HttpResponse('<h1>Autenticação de Usuários (Login/Cadastro)</h1>')

def sobre(request):
    return render(request, 'plataforma/sobre.html')

# def listar_cursos(request):
#     curso = Curso.objects.all()
#     return render(request, 'plataforma/home.html', {'cursos':curso})