from django import forms
from ..models import Proveedores
#tupla contiene dos elementos 1. valor que se envia 2. texto se se muestra
_opciones:list = [(True, 'Activo'), (False, 'Inactivo')]

    
class MarcaForm(forms.Form):
    _proveedores:Proveedores = Proveedores.objects.values_list('id_proveedor','nombre_vendedor')  
    nombrombemarca = forms.CharField(
        label='Nombre Marca', 
        max_length=100,
        widget = forms.TextInput(attrs={'id':'in_nombre'}),
        )
    descripcion = forms.CharField(
        label='Descripción', 
        max_length=255,
        widget = forms.TextInput(attrs={'id':'in_descripcion'})
        )
    estado = forms.ChoiceField(
        label='Estado', 
        choices=_proveedores
       )


# formulario de Categorias

class CategoriaForm(forms.Form):
    nombreCategoria = forms.CharField(
        label='Nombre Categoria', 
        max_length=100,
        widget = forms.TextInput(attrs={'id':'in_nombre'}),
        )
    descripcion = forms.CharField(
        label='Descripción', 
        max_length=255,
        widget = forms.TextInput(attrs={'id':'in_descripcion'})
        )
    estado = forms.ChoiceField(
        label='Estado', 
        choices=_opciones
       )
    
# formulario compras

class ComprasForm(forms.Form):
    _proveedores:Proveedores = Proveedores.objects.values_list('id_proveedor','nombre_vendedor')
    _p:Proveedores = Proveedores.objects.values_list('id_proveedor','nombre_vendedor')
    fechaCompra = forms.DateField(
        label='Fecha Compra',
        widget=forms.DateInput(attrs={'id': 'in_fecha', 'type': 'date'}),
        input_formats=['%Y-%m-%d'], 
        )
    proveedor = forms.ChoiceField(
        label='Proveedores', 
        choices=_proveedores
      )

    empleado = forms.CharField(
        label='empleado', 
        max_length=255,
        widget = forms.TextInput(attrs={'id':'in_proveedor'})
        )
    estado = forms.ChoiceField(
        label='Estado', 
        choices=_proveedores
       )