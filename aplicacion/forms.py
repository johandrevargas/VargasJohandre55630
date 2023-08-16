from django import forms


class formularioinforme(forms.Form):
    nombre_informes = forms.CharField(max_length=50, required=True)
    equipo_responsable_informe = forms.CharField(max_length=15, required=True)
