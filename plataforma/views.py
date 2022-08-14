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

def curso(request, id_curso):
    # curso = Curso.objects.filter(id=id_curso)
    curso = Curso.objects.get(id=id_curso)
    return render(request, 'plataforma/curso.html', {'curso':curso})
    # return HttpResponse(curso.descricao)

def disciplinas(request):
    # curso = Curso.objects.all()
    return render(request, 'plataforma/lista_disciplinas.html')