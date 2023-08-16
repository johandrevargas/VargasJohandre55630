# Generated by Django 4.2.4 on 2023-08-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplicacion", "0003_rename_correo_usuarios_correo_usuarios_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="informes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_informes", models.CharField(max_length=50)),
                (
                    "equipo_responsable_informe",
                    models.CharField(default="usuario", max_length=15),
                ),
            ],
        ),
        migrations.CreateModel(
            name="secciones_informes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre_informes", models.CharField(max_length=50)),
                ("variable_informe", models.BooleanField()),
                ("generacion", models.BooleanField()),
                ("demanda", models.BooleanField()),
                ("precios_bolsa", models.BooleanField()),
                ("precios_oferta", models.BooleanField()),
                ("embalses", models.BooleanField()),
                ("aportes", models.BooleanField()),
            ],
        ),
    ]