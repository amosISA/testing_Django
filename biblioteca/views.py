# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render

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
    return render(request, 'biblioteca/meta_items.html', {'items':valor, 'ruta':path})