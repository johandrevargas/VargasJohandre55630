from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuarios(models.Model):
    correo_usuarios = models.CharField(max_length = 30)
    password_usuarios = models.CharField(max_length = 15, default= 'password')


class Informes(models.Model):
    nombre_informes = models.CharField(max_length = 50)
    equipo_responsable_informe = models.CharField(max_length = 15, default= 'usuario')


class Secciones_Informes(models.Model):
    nombre_informes = models.CharField(max_length = 50)
    variable_informe = models.BooleanField()
    generacion = models.BooleanField()
    demanda = models.BooleanField()
    precios_bolsa = models.BooleanField()
    precios_oferta = models.BooleanField()
    embalses = models.BooleanField()
    aportes = models.BooleanField()


class TipoInformes(models.Model): 
    tipo_informe = models.CharField(max_length=50)


class Equipos(models.Model):
    equipo = models.CharField(max_length= 50)
    usuario_responsable = models.CharField(max_length = 50)


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"