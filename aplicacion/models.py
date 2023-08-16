from django.db import models

# Create your models here.

class usuarios(models.Model):
    correo_usuarios = models.CharField(max_length = 30)
    password_usuarios = models.CharField(max_length = 15, default= 'password')


class informes(models.Model):
    nombre_informes = models.CharField(max_length = 50)
    equipo_responsable_informe = models.CharField(max_length = 15, default= 'usuario')


class secciones_informes(models.Model):
    nombre_informes = models.CharField(max_length = 50)
    variable_informe = models.BooleanField()
    generacion = models.BooleanField()
    demanda = models.BooleanField()
    precios_bolsa = models.BooleanField()
    precios_oferta = models.BooleanField()
    embalses = models.BooleanField()
    aportes = models.BooleanField()
