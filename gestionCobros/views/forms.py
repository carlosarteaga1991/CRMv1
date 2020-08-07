from django.forms import *
from gestionCobros.models import Departamentos, Usuarios

class dep_form(ModelForm):
    class Meta:
        model = Departamentos
        fields = '__all__'
        exclude = ['fch_modificacion','usuario_modificacion','fch_creacion','usuario_creacion'] # en casoi que no deseemos que un campo se muestre
        widgets = {
            'nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),

            'estado': Select(
                attrs={
                    'class': 'form-control',
                    #'size': '10'
                }
            )
        }

class user_form(ModelForm):

    class Meta:
        model = Usuarios
        fields = '__all__'
        exclude = ['fch_modificacion','usuario_modificacion','fch_creacion','usuario_creacion','ip_ultimo_acceso','fch_ultimo_acceso'] # en casoi que no deseemos que un campo se muestre
        widgets = {
            'primer_nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    #'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'segundo_nombre': TextInput(
                attrs={
                    'class': 'form-control',
                    #'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'primer_apellido': TextInput(
                attrs={
                    'class': 'form-control',
                    #'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'segundo_apellido': TextInput(
                attrs={
                    'class': 'form-control',
                    #'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'usuario': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ejemplo: nombre.apellido',
                    'autocomplete': 'off'
                }
            ),
            'correo': EmailInput(
                attrs={
                    'class': 'form-control',
                    #'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'telefono': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'id_departamento': Select(
                attrs={
                    'class': 'form-control',
                    #'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'id_puesto': Select(
                attrs={
                    'class': 'form-control',
                    #'placeholder': 'Ingrese Nombre del Departamento',
                    'autocomplete': 'off'
                }
            ),
            'estado': Select(
                attrs={
                    'class': 'form-control',
                    #'size': '10'
                }
            )
        }


