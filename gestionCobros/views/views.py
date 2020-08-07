
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,CreateView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required
from gestionCobros.views.forms import *
from gestionCobros.models import Clientes, Departamentos,Usuarios
#para decoradores en python
#
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
        #print(reverse_lazy('v3'))
        return context

class dep_crear(CreateView):
    model = Departamentos
    form_class = dep_form
    template_name = 'departamento/create.html'
    success_url = reverse_lazy('v3') #esto una vez q se guardó el registro que vuelva atrás o le decimos a donde lo envíe



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # x defecto
        context['title'] = 'Crear Departamento'
        return context


class user_listar(ListView):
    model = Usuarios  # le decimo que el modelo es la tabla Departamento
    template_name = 'usuario/listar.html' # le decimos a esta variable donde está

    #@method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request,*args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request,*args, **kwargs):
        data = {}
        try:
            data = Departamentos.objects.get(pk=request.POST['id_usuario']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # x defecto
        context['title'] = 'Listado de Usuarios'
        return context

class user_crear(CreateView):
    model = Usuarios
    form_class = user_form
    template_name = 'usuario/create.html'
    success_url = reverse_lazy('v5') #esto una vez q se guardó el registro que vuelva atrás o le decimos a donde lo envíe


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # x defecto
        context['title'] = 'Crear Usuario'
        return context