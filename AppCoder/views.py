from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse ('vista inicio')
def cursos(request):
    return HttpResponse('vista cursos')
def entregables(request):
    return HttpResponse('vista entregables')
def profesores(request):
    return HttpResponse('vista profesores')
def estudiantes(request):
    return HttpResponse('vista estudiantes')



def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada=12345)
    curso.save()
    documentoDeTexto= f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documentoDeTexto)