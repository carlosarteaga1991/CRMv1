from django.contrib import admin
from gestionCobros.models import Puestos, Departamentos, Usuarios, Empresas, Clientes, Contactos, Productos, Recordatorios, Codigos, Motivos, Gestiones, Promesas, Pagos, LogCobros

# se puede agregar también from gestionCobros.models import *
#Clientes, Gestiones, Codigos,Motivos,Recordatorios

# Register your models here.

"""
# COMENTARIO#A1 para que desde el panel de administración tengamos disponible la tabla clientes
# otros campos agregamos la paralbra reservada después de Clientes "ClientesAdmin" (para manipular las clases desde el panel de administración)

# y creamos :
class ClientesAdmin(admin.ModelAdmin):
    list_display = ("id_cliente","primer_nombre","segundo_nombre","primer_apellido","segundo_apellido","correo","estatus")
    search_fields = ("primer_apellido","id_cliente","primer_nombre") # esto para hacer búsqueda por diferentes campos

class CodigitoAdministrar(admin.ModelAdmin):
    list_filter = ("descrip_codigo",) # OJO se agrega una coma al final ya que es una tupla, esto me servirá bastante
    # para filtrar los clientes por empresa a manera de ejemplo o x FECHA

    # si deseamos hacer un filtro específico de fecha cemos ésto:
    # date_hierarchy = "fecha"


admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Gestiones)
admin.site.register(Codigos,CodigitoAdministrar)
admin.site.register(Motivos)
admin.site.register(Recordatorios)
"""

admin.site.register(Puestos)
admin.site.register(Departamentos)
admin.site.register(Usuarios)
admin.site.register(Empresas)
admin.site.register(Clientes)
admin.site.register(Contactos)
admin.site.register(Productos)
admin.site.register(Recordatorios)
admin.site.register(Codigos)
admin.site.register(Motivos)
admin.site.register(Gestiones)
admin.site.register(Promesas)
admin.site.register(Pagos)
admin.site.register(LogCobros)