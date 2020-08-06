"""CRMv1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestionCobros.views.views import *
#Vistauno,Vistados,departamento_lista


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('vistas/', Vistauno, name='v1'),
    #path('second/',Vistados, name='v2'),
    path('departamento/listar',dep_lista.as_view(), name='v3') #aquí lo que hacemos es llamar una clase vista para usarla en una plantilla
]
