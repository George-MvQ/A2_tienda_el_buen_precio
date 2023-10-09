from django import forms
from administracion_app.models import Proveedores,  Empleados, MetodosPago, Productos

#tupla contiene dos elementos 1. valor que se envia 2. texto se se muestra
_opciones:list = [(True, 'Activo'), (False, 'Inactivo')]


class MarcaForm(forms.Form):
    # _proveedores:Proveedores = Proveedores.objects.values_list('id_proveedor','nombre_vendedor')
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

# formulario compras

class ComprasForm(forms.Form):
    _proveedores:Proveedores = Proveedores.objects.values_list('id_proveedor','nombre_vendedor')
    _empleado:Empleados = Empleados.objects.values_list('id_empleado','primer_nombre')
    _metodopago:MetodosPago = MetodosPago.objects.values_list('id_metodo_pago','nombre')
    fechaCompra = forms.DateField(
        label='Fecha Compra',
        widget=forms.DateInput(attrs={'id': 'in_fecha', 'type': 'date','format': '%d/%m/%Y'}),
        input_formats=['%d/%m/%Y'],
        )
    proveedor = forms.ChoiceField(
        label='Proveedores',
        choices=_proveedores
      )
    empleado = forms.ChoiceField(
        label='Empleado',
        choices=_empleado
      )
    metodopago = forms.ChoiceField(
        label='Metodo de Pago',
        choices=_metodopago
      )
    observaciones = forms.CharField(
        label='observaciones',
        max_length=255,
        widget = forms.TextInput(attrs={'id':'in_observaciones'})
        )
""" DETALLE COMPRA"""
class DetalleForm(forms.Form):
        _producto:Productos = Productos.objects.values_list('id_productos','nombre_producto')

        detallecompra = forms.CharField(
            label='Id Detalle Compra',
            max_length=100,
            widget = forms.TextInput(attrs={'id':'in_detalle'}),
        )
        producto = forms.ChoiceField(
            label='Nombre Producto',
            choices=_producto
        )
        compras = forms.CharField(
            label='Compras',
            max_length=100,
            widget = forms.TextInput(attrs={'id':'in_compras'}),
        )
        descuentos = forms.CharField(
            label='Descuentos',
            max_length=100,
            widget = forms.TextInput(attrs={'id':'in_descuentos'}),
        )
        cantidad = forms.CharField(
            label='Cantidad',
            max_length=100,
            widget = forms.TextInput(attrs={'id':'in_cantidad'}),
        )
        preciounitario = forms.CharField(
            label='Precio Unitario Compra',
            max_length=100,
            widget = forms.TextInput(attrs={'id':'in_preciounitario'}),
        )
        preciosugerido = forms.CharField(
            label='Precio de Venta',
            max_length=100,
            widget = forms.TextInput(attrs={'id':'in_precioventa'}),
        )
        numerolote = forms.CharField(
            label='No lote',
            max_length=100,
            widget = forms.TextInput(attrs={'id':'in_lote'}),
        )



class CategoriaForm(forms.Form):
        nombrecategoria = forms.CharField(
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

class ProveedoresForm(forms.Form):
        nombrevendedor = forms.CharField(
        label='Nombre Proveedor',
        max_length=100,
        widget = forms.TextInput(attrs={'id':'in_nombre'}),
        )
        telefono = forms.CharField(
        label='Telefono',
        max_length=20,
        widget = forms.TextInput(attrs={'id':'in_telefono'}),
        )
        diavisita = forms.DateField(
        label='Dia de visita',
        widget=forms.DateInput(attrs={'id': 'in_fechavi', 'type': 'date','format': '%d/%m/%Y'}),
        input_formats=['%d/%m/%Y'],
        )
        diaentrega = forms.DateField(
        label='Dia de entrega',
        widget=forms.DateInput(attrs={'id': 'in_fechavi', 'type': 'date','format': '%d/%m/%Y'}),
        input_formats=['%d/%m/%Y'],
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


class UsuarioForm(forms.Form):
    nombre_usuario = forms.CharField(
        label='Nombre de usuario',
        max_length=100,
        widget = forms.TextInput(attrs={'id':'in_nombre'}),
    )

    contrasenia = forms.CharField(
        label='Contraseña',
        max_length=100,
        widget = forms.PasswordInput(attrs={'id':'in_contra'}),

    )

    correo = forms.CharField(
        label='Correo',
        max_length=255,
        widget = forms.EmailInput (attrs={'id':'in_correo'})
        )

    estado = forms.ChoiceField(
        label='Estado',
        choices=_opciones
       )

    super_usuario = forms.ChoiceField(
        label='Estado',
        choices=_opciones
       )



class listadoForm(forms.Form):
        _empleado:Empleados = Empleados.objects.values_list('id_empleado','primer_nombre')
        fechacreacion = forms.DateField(
        label='Fecha Creacion',
        widget=forms.DateInput(attrs={'id': 'in_fechavi', 'type': 'date','format': '%d/%m/%Y'}),
        input_formats=['%d/%m/%Y'],
        )
        empleado = forms.ChoiceField(
        label='Empleado',
        choices=_empleado
        )
        estado = forms.ChoiceField(
        label='Estado',
        choices=_opciones
       )



""" password = models.CharField(max_length=128, db_collation='Modern_Spanish_CI_AS')
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Modern_Spanish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Modern_Spanish_CI_AS')
    is_active = models.BooleanField()
"""
