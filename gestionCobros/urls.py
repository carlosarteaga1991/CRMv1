from django.urls import path
from gestionCobros.views.views import *

#app_name = 'e'

urlpatterns = [
    path('listar/',dep_lista.as_view(), name='v3'), #aquí lo que hacemos es llamar una clase vista para usarla en una plantilla
    path('crear/',dep_crear.as_view(), name='v4'),
    path('listar2/',user_listar.as_view(), name='v5'),
    path('crear2/',user_crear.as_view(), name='v6')    
]
