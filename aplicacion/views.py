from django.shortcuts import render
from django.http import HttpResponse
from .models import usuarios
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request, "aplicacion/listado_informes.html")

def login(request):
    return render(request, "aplicacion/login.html")

def registrar_usuario(request):
    return render(request, "aplicacion/registrar_usuario.html")

def validacion_ingreso_informes(request):
     return render(request, "aplicacion/validacion_ingreso_informes.html")

def consultar_informes(request):
    return render(request, "aplicacion/consultar_informes.html")

def listado_informes(request):
    contexto = {'Informes': informes.objects.all()}
    return render(request, "aplicacion/listado_informes.html", contexto)

def buscar_informes(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        contexto = {"Informes": informes.objects.filter(nombre_informes__icontains=patron)}
        return render(request, "aplicacion/listado_informes.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

def ingresar_informes(request):
    if request.method == "POST":
        miForm = formularioinforme(request.POST)
        if miForm.is_valid():
            insert_nombre_informe = miForm.cleaned_data.get('nombre_informes')
            insert_equipo_responsable_informe = miForm.cleaned_data.get('equipo_responsable_informe')
            informe_insert = informes(nombre_informes = insert_nombre_informe, equipo_responsable_informe= insert_equipo_responsable_informe)
            informe_insert.save()
            return render(request, "aplicacion/validacion_ingreso_informes.html")
    else:
        miForm = formularioinforme()
    return render(request, "aplicacion/ingresar_informes.html", {"form": miForm })





