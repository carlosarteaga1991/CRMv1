from django.db import models

# Modificación de modelos con relaciones realzada el 1 de agosto del 2020 a las 11:42 am

# se crearán 14 tablas relacionadas conectándose a MYSQL
# las tablas seran:

"""
Usuarios
Departamentos
Puestos
Clientes
Empresas
Productos
Contactos
Gestiones
Códigos
Motivos
Recordatorios
Promesas
Pagos
Log_Cobros
"""


class Departamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField()
    fch_modificacion = models.CharField(max_length=35, blank=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos"
        ordering = ['id_departamento']

class Puestos(models.Model):
    id_puesto = models.AutoField(primary_key=True)
    id_departamento = models.ForeignKey(Departamentos, on_delete=models.PROTECT) #protege en caso de querer borrar
    nombre = models.CharField(max_length=100)
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField()
    fch_modificacion = models.CharField(max_length=35, blank=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Puestos" #para que no le agrega una ese en el admin panel de django
        ordering = ['id_puesto']

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=35)
    segundo_nombre = models.CharField(max_length=35,blank=True) # verificar si no es obligatorio sino agregar, null=True
    primer_apellido = models.CharField(max_length=35)
    segundo_apellido = models.CharField(max_length=35, blank=True)
    usuario = models.CharField(max_length=20,help_text="Ejemplo: nombre.apellido")
    correo = models.EmailField()
    telefono = models.IntegerField()
    id_departamento = models.ForeignKey(Departamentos, on_delete=models.PROTECT)
    id_puesto = models.ForeignKey(Puestos, on_delete=models.PROTECT)
    fch_ultimo_acceso = models.DateTimeField()
    ip_ultimo_acceso = models.CharField(max_length=50)
    fch_creacion = models.DateTimeField(auto_now_add=True)
    usuario_creacion = models.IntegerField()
    fch_modificacion = models.CharField(max_length=35, blank=True)
    usuario_modificacion = models.IntegerField(blank=True,null=True)
    estado = models.CharField(max_length=1, default='1',choices=[('1','Activo'),('2','Inactivo')])

    def __str__(self):
        return self.primer_nombre + " " + self.segundo_nombre + " " + self.primer_apellido + " " + self.segundo_apellido
    
    class Meta:
        verbose_name_plural = "Usuarios"
        ordering = ['primer_nombre']


    
