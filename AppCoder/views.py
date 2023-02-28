from django.shortcuts import render
#from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'index.html')
def cursos(request):
    return render(request, 'cursos.html')
def entregables(request):
    return render(request, 'entregables.html')
def profesores(request):
    return render(request, 'profesores.html')
def estudiantes(request):
    return render(request, 'estudiantes.html')


'''
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada=12345)
    curso.save()
    documentoDeTexto= f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documentoDeTexto)
'''