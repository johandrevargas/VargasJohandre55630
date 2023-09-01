from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from search_views.search import SearchListView
from search_views.filters import BaseFilter

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.views.generic import TemplateView, ListView

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html")

# def login(request):
#     return render(request, "aplicacion/login.html")
@login_required
def registrar_usuario(request):
    return render(request, "aplicacion/registrar_usuario.html")

@login_required
def validacion_ingreso_informes(request):
     return render(request, "aplicacion/validacion_ingreso_informes.html")

@login_required
def consultar_informes(request):
    return render(request, "aplicacion/consultar_informes.html")

@login_required
def sobre_mi(request):
    return render(request, "aplicacion/sobre_mi.html")

@login_required
def listado_informes(request):
    contexto = {'Informes': Informes.objects.all()}
    return render(request, "aplicacion/listado_informes.html", contexto)

# def informes(request):
#     contexto = {'informes': Informes.objects.all()}
#     return render(request, "aplicacion/informes.html", contexto)

################
#   ejecuciones
################
@login_required
def buscar_informes(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        contexto = {"Informes": Informes.objects.filter(nombre_informes__icontains=patron)}
        return render(request, "aplicacion/listado_informes.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

@login_required
def ingresar_informes(request):
    if request.method == "POST":
        miForm = formularioinforme(request.POST)
        if miForm.is_valid():
            insert_nombre_informe = miForm.cleaned_data.get('nombre_informes')
            insert_equipo_responsable_informe = miForm.cleaned_data.get('equipo_responsable_informe')
            informe_insert = Informes(nombre_informes = insert_nombre_informe, equipo_responsable_informe= insert_equipo_responsable_informe)
            informe_insert.save()
            return render(request, "aplicacion/validacion_ingreso_informes.html")
    else:
        miForm = formularioinforme()
    return render(request, "aplicacion/ingresar_informes.html", {"form": miForm })


# def update_informe_solicitado(request, id_informes):
#     informe = informes.objects.get(id=id_informes)
#     if request.method == "POST":
#         miForm = informesForm(request.POST)
#         if miForm.is_valid():
#             informe.nombre_informes = miForm.cleaned_data.get('nombre_informes')
#             informe.equipo_responsable_informe = miForm.cleaned_data.get('equipo_responsable_informe')
#             informe.save()
#             return redirect(reverse_lazy('solicitar_informes'))
#     else:
#         miForm = informesForm(initial={
#             'nombre_informe': informe.nombre_informes,
#             'equipo_responsable_informes': informe.equipo_responsable_informe,
#         })
#     return(request, "aplicacion/informesForm.html", {'form': miForm})


# def deleteInformes(request, id_informe):
#     informe = informes.objects.get(id = id_informe)
#     informe.delete()
#     return redirect(reverse_lazy('informes'))


# ________________ Class Based View ________________ #

################################
#   ____    INFORMES   ____    #
################################
class InformesList(LoginRequiredMixin, ListView):
    model = Informes

class InformesCreate(LoginRequiredMixin, CreateView):
    model = Informes
    fields = ['nombre_informes', 'equipo_responsable_informe']
    success_url = reverse_lazy('informes')

class InformesUpdate(LoginRequiredMixin, UpdateView):
    model = Informes
    fields = ['nombre_informes', 'equipo_responsable_informe']
    success_url = reverse_lazy('informes')

class InformesDelete(LoginRequiredMixin, DeleteView):
    model = Informes
    success_url = reverse_lazy('informes')

################################
#   ____    USUARIOS   ____    #
################################
class UsuariosList(LoginRequiredMixin, ListView):
    model = Usuarios

class UsuariosCreate(LoginRequiredMixin, CreateView):
    model = Usuarios
    fields = ['correo_usuarios', 'password_usuarios']
    success_url = reverse_lazy('usuarios')

class UsuariosUpdate(LoginRequiredMixin, UpdateView):
    model = Usuarios
    fields = ['correo_usuarios', 'password_usuarios']
    success_url = reverse_lazy('usuarios')

class UsuariosDelete(LoginRequiredMixin, DeleteView):
    model = Usuarios
    success_url = reverse_lazy('usuarios')


####################################
#   ____    TIPO INFORME   ____    #
####################################
class TipoInformesList(LoginRequiredMixin, ListView):
    model = TipoInformes

class TipoInformesCreate(LoginRequiredMixin, CreateView):
    model = TipoInformes
    fields = ['tipo_informe']
    success_url = reverse_lazy('tipoinforme')

class TipoInformesUpdate(LoginRequiredMixin, UpdateView):
    model = TipoInformes
    fields = ['tipo_informe']
    success_url = reverse_lazy('tipoinforme')

class TipoInformesDelete(LoginRequiredMixin, DeleteView):
    model = TipoInformes
    success_url = reverse_lazy('tipoinforme')


###############################
#   ____    EQUIPOS   ____    #
###############################
class EquiposList(LoginRequiredMixin, ListView):
    model = Equipos

class EquiposCreate(LoginRequiredMixin, CreateView):
    model = Equipos
    fields = ['equipo', 'usuario_responsable']
    success_url = reverse_lazy('equipos')

class EquiposUpdate(LoginRequiredMixin, UpdateView):
    model = Equipos
    fields = ['equipo', 'usuario_responsable']
    success_url = reverse_lazy('equipos')

class EquiposDelete(LoginRequiredMixin, DeleteView):
    model = Equipos
    success_url = reverse_lazy('equipos')



###############
#   SEARCH    #
###############
class InformesFilter(LoginRequiredMixin, BaseFilter):
    search_fields = {
        'search_text' : ['nombre_informes', 'equipo_responsable_informe'],
        'nombre_informes' : { 'operator' : '__exact', 'fields' : ['nombre_informes'] },
        'equipo_responsable_informe' : { 'operator' : '__gte', 'fields' : ['equipo_responsable_informe'] },
    }

class InformesSearchList(LoginRequiredMixin, SearchListView):
    model = Informes
    paginate_by = 30
    template_name = "aplicacion/informes_list.html"
    form_class = InformesSearchForm
    filter_class = InformesFilter

# ________________ Login / Logout ________________ #

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data = request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/home.html")
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son invalidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son invalidos'})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm})





