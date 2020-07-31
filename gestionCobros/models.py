from django.db import models

# Create your models here.

#si deseamos que en el panel de administración nos aparezca otros campos al visualizar una tabla ver el archivo
#admin.py en el COMENTARIO#A1

# comentario agregado el 31 de julio a las 2:35 pm para verificar q se cré corectamente

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30,blank=True) # blanck es para decirle q acepte dejarlo en blanco
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30,blank=True)
    correo = models.EmailField(verbose_name='Email Institucional')
    telefono = models.IntegerField()
    Nacionalidad =models.CharField(max_length=35,null=True,help_text='Ejemp: hondureño, estadounidense, canadiense')#editable=False
    #las dos últimas instrucciones son para q el campo no sea obligatorio
    # si colocamos editable=False no se mostrará en el administrador de django es bueno para las bitácoras ,editable=False
    estatus = models.CharField(max_length=1, default=1, choices=[('1','Activo'),('2','Inactivo')])
    imagencliente = models.ImageField(upload_to='fotosclientes',blank=True)  

    def __str__(self):
        return self.primer_nombre + " " + self.segundo_nombre + " " + self.primer_apellido + " " + self.segundo_apellido 
    
    class Meta:
        #verbose_name='Clientes'
        verbose_name_plural='Clientes' #para q aparezca como queramos en el administrador de DJANGO
        #db_table='clientes'
        ordering=['id_cliente']

class Gestiones(models.Model):
    id_gestion = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    fch_gestion = models.DateField(auto_now_add=True)
    hora_gestion = models.TimeField(auto_now_add=True)
    id_codigo = models.IntegerField()
    id_motivo = models.IntegerField()
    descrip_gestion = models.TextField()
    estatus = models.CharField(max_length=1, default=1)

class Recordatorios(models.Model):
    id_recordatorio = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    fch_recordatorio = models.DateField()
    hora_recordatorio = models.TimeField()
    descrip_recordatorio = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return 'el cliente %s tiene un recordatorio para el %s, a las %s ' % (self.id_cliente,self.fch_recordatorio,self.hora_recordatorio)

    
class Codigos(models.Model):
    id_codigo = models.AutoField(primary_key=True)
    descrip_codigo = models.CharField(max_length=100)
    estatus = models.CharField(max_length=1, default=1)

class Motivos(models.Model):
    id_motivo = models.AutoField(primary_key=True)
    descrip_motivo = models.CharField(max_length=100)
    estatus = models.CharField(max_length=1, default=1)