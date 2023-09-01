# Generated by Django 4.2.4 on 2023-08-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aplicacion", "0004_informes_secciones_informes"),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipos",
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
                ("equipo", models.CharField(max_length=50)),
                ("usuario_responsable", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TipoInformes",
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
                ("tipo_informe", models.CharField(max_length=50)),
            ],
        ),
    ]