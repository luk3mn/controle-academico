from tkinter import CASCADE
from django.db import models
from django.forms import CharField

class Curso(models.Model):
    descricao = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

class Disciplina(models.Model):
    descricao = models.CharField(max_length=100)
    turma = models.CharField(max_length=15)
    data_criacao = models.DateTimeField(max_length=True)
    # professor = models.ForeignKey()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao