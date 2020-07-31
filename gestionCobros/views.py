from django.shortcuts import render

# Create your views here.
class Cliente(object):
    def __init__(self,nombre1,nombre2,apellido1,apellido2,correo,telefono):
        self.primer_nombre=nombre1
        self.segundo_nombre=nombre2
        self.primero_apellido=apellido1
        self.segundo_apellido=apellido2
        self.correo=correo
        self.telefono=telefono

