
from django.urls import path, include
from .views import *



urlpatterns = [
    path('', listado_informes, name= "listado_informes"),
    path('home/', listado_informes, name= "home"),
    path('login/', login, name= 'login'),
    path('ingresar_informes/', ingresar_informes, name= 'ingresar_informes'),
    path('consultar_informes/', consultar_informes, name= 'consultar_informes'),
    path('buscar_informes/', buscar_informes, name= 'buscar_informes'),
    path('listado_informes/', listado_informes, name= 'listado_informes'),
]