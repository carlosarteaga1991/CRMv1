
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from gestionCobros.models import Clientes, Departamentos

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
#para decoradores en python





"""
def Vistauno(request):
    data1={"cliente":Clientes.objects.all()}
    return render(request,'home.html', data1) 


def Vistados(request):
    dato1 = { 'dep': Departamentos.objects.all()}
    return render(request, 'secundario.html',dato1)
    from django.shortcuts import render


def departamento_lista(request):
    data = {'title': 'Listado de departamentos',
    'dep': Departamentos.objects.all()}
    return render(request, 'departamento/listar.html', data)
"""
#vistas basadas en clases

class dep_lista(ListView):
    model = Departamentos  # le decimo que el modelo es la tabla Departamento
    template_name = 'departamento/listar.html' # le decimos a esta variable donde está

    #@method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        data = {}
        try:
            data = Departamentos.objects.get(pk=request.POST['id_departamento']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # x defecto
        context['title'] = 'Listado de Departamentos'
        return context

