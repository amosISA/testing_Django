"""genuinescore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from genuinescore.views import hola, raiz, horas_adelante, fecha_actual
from biblioteca import views

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^hola/', hola),
    url(r'^$', raiz),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante),
    url(r'^fecha/actual/$', fecha_actual),
    url(r'^nav/$', views.mostrar_naveador),
    url(r'^items/nav/$', views.mostrar_request_items),
    url(r'^formulario-buscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar),
]
