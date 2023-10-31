from django import forms
from administracion_app.models import Ventas, Productos, DetalleVentas




class Ventasform(forms.ModelForm):
    class Meta:
        model = DetalleVentas
        fields = ['fk_id_producto1']
        labels = {

            'fk_id_producto1' :'Producto'
      
        }