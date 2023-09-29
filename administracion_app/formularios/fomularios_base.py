from django import forms

#tupla contiene dos elementos 1. valor que se envia 2. texto se se muestra
_opciones:list = [(True, 'Activo'), (False, 'Inactivo')]
    
class MarcaForm(forms.Form):
    nombremarca = forms.CharField(
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
        choices=_opciones
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