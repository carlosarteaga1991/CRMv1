
from django.shortcuts import render

from gestionCobros.models import Clientes, Departamentos


#

def Vistauno(request):
    data1={"cliente":Clientes.objects.all()}
    return render(request,'home.html', data1) 


def Vistados(request):
    dato1 = { 'dep': Departamentos.objects.all()}
    return render(request, 'secundario.html',dato1)