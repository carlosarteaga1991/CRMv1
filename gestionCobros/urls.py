from django.urls import path
from gestionCobros.views.views import *

#app_name = 'e'

urlpatterns = [
    path('listar/',dep_lista.as_view(), name='v3'), #aquí lo que hacemos es llamar una clase vista para usarla en una plantilla
    path('crear/',dep_crear.as_view(), name='v4')
]
