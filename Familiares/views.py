from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, Template, loader

from Familiares.models import Familiares

# Create your views here.


def inicio(request):
    return HttpResponse('PAGINA PRINCIPAL DE PROYECTO CODER')

def listado_familiares(request):

    template = loader.get_template("template.html")

    lista_familiares = Familiares.objects.all()

    render = template.render({"lista": lista_familiares})

    return HttpResponse(render)
