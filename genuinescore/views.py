from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def hola(request):
    return HttpResponse("Hola Mundo")

def raiz(request):
    return HttpResponse("<h1 style='color:red'>Bienvenidos a GenuineScore</h1>")

def fecha_actual(request):
    ahora = datetime.datetime.now()
    return render(request, 'fecha_actual.html', {'fecha_actual': ahora})

def horas_adelante(request, horas):
    try:
        horas = int(horas)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now()+datetime.timedelta(hours=horas)
    return render(request, 'horas_adelante.html', {'hora_siguiente':dt,'horas':horas})
