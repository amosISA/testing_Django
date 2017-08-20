# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from biblioteca.models import Libro

# Create your views here.
def mostrar_naveador(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Tu navegador es %s" % ua)

def mostrar_request_items(request):
    valor = request.META.items()
    valor.sort()
    path = request.path
    return render(request, 'meta_items.html', {'items':valor, 'ruta':path})

def formulario_buscar(request):
    return render(request, 'formulario_buscar.html')

def buscar(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q: #si cuando visitas el formulario el input esta vacio
            errors.append("Por favor introduce un término de búsqueda válido!")
        elif len(q) > 20:
            errors.append("Por favor introduce un término de búsqueda inferior a 20 caracteres.")
        else:
            libros = Libro.objects.filter(titulo__icontains=q)
            return render(request, 'resultados.html', {'libros':libros, 'query':q})

    return render(request, 'formulario_buscar.html', {'errors':errors})