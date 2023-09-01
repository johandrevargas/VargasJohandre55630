
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',home, name= "home"),
    path('home/', home, name= "home"),
    path('login/', login_request, name= 'login'),
    path('ingresar_informes/', ingresar_informes, name= 'ingresar_informes'),
    path('consultar_informes/', consultar_informes, name= 'consultar_informes'),
    path('buscar_informes/', buscar_informes, name= 'buscar_informes'),
    path('listado_informes/', listado_informes, name= 'listado_informes'),
#    path('informes/', Informes, name= 'informes'),

#    path('update_informe_solicitado/<id_informes>/', update_informe_solicitado, name= 'update_informe_solicitado'),
    # path('deleteInformes/<id_informes>/', deleteInformes, name= 'deleteInformes'),

    path('informes/', InformesList.as_view(), name='informes'),
    path('create_informes/', InformesCreate.as_view(), name='create_informes'),
    path('update_informes/<int:pk>/', InformesUpdate.as_view(), name='update_informes'),
    path('delete_informes/<int:pk>/', InformesDelete.as_view(), name='delete_informes'),


    path('usuarios/', UsuariosList.as_view(), name='usuarios'),
    path('create_usuarios/', UsuariosCreate.as_view(), name='create_usuarios'),
    path('update_usuarios/<int:pk>/', UsuariosUpdate.as_view(), name='update_usuarios'),
    path('delete_usuarios/<int:pk>/', UsuariosDelete.as_view(), name='delete_usuarios'),


    path('tipoinforme/', TipoInformesList.as_view(), name='tipoinforme'),
    path('create_tipoinforme/', TipoInformesCreate.as_view(), name='create_tipoinforme'),
    path('update_tipoinforme/<int:pk>/', TipoInformesUpdate.as_view(), name='update_tipoinforme'),
    path('delete_tipoinforme/<int:pk>/', TipoInformesDelete.as_view(), name='delete_tipoinforme'),


    path('equipos/', EquiposList.as_view(), name='equipos'),
    path('create_equipos/', EquiposCreate.as_view(), name='create_equipos'),
    path('update_equipos/<int:pk>/', EquiposUpdate.as_view(), name='update_equipos'),
    path('delete_equipos/<int:pk>/', EquiposDelete.as_view(), name='delete_equipos'),


    path('sobre_mi/', sobre_mi, name= 'sobre_mi'),
    path("search/", InformesSearchList.as_view(), name="informes"),
    path('registro/', register, name="registro" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/home.html"), name="logout" ),
]