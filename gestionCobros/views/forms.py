from django.forms import ModelForm
from gestionCobros.models import Departamentos

class dep_form(ModelForm):
    class Meta:
        model = Departamentos
        fields = '__all__'
        #exclude = ['fecha_modificación'] # en casoi que no deseemos que un campo se muestre

