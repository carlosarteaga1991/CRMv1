from django.contrib import admin
from gestionCobros.models import Puestos, Departamentos, Usuarios
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