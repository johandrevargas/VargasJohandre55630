from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formularioinforme(forms.Form):
    nombre_informes = forms.CharField(max_length=50, required=True)
    equipo_responsable_informe = forms.CharField(max_length=15, required=True)


# class InformesForm(forms.Form):
#     nombre_informe = forms.CharField(label = "Nombre Informe",max_length = 50, required= False)
#     equipo_informe = forms.CharField(label = "Equipo Informe", max_length= 50)

class InformesSearchForm(forms.Form):
    nombre_informes =  forms.CharField(
                    required = False,
                    label='Ingresar el nombre del informe',
                    widget=forms.TextInput(attrs={'placeholder': 'Informe a Buscar'})
                  )

    equipo_responsable_informe = forms.CharField(
                    required = False,
                    label='Ingresar el equipo responsable'
                  )
  

class RegistroUsuariosForm(UserCreationForm):      
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
