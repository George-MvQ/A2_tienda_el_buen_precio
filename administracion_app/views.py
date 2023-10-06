from django.shortcuts import render,redirect
#from administracion_app.models import *
""" from inicio_app.models import AuthUser """
from django.http import JsonResponse
from .formularios.fomularios_base import MarcaForm
from .formularios.fomularios_base import CategoriaForm
from .formularios.fomularios_base import ComprasForm
from django.views import View
from .validaciones import *
import json 

def admon(request):

    return render(request, 'adminuser/inicio/inicio_admin.html')

""" En este apartado nosotro estamos administrando los usuarios de nuestro sistema  """

#
def administrar_usuarios(request):
    mantenimiento = MantenimientoUsuario()
    if request.method == 'GET':
        usuarios:list = mantenimiento.obtener_usuarios()
        return render(request, 'adminuser/administrativo/administrativo.html', {'usuarios':usuarios})
    
    elif request.method == 'POST':
        form = MarcaForm(request.POST)
        respuesta:dict = ingeso_marca(form)
        return JsonResponse(respuesta)
    
    elif request.method == 'DELETE':
        dato_obtenido = json.loads(request.body)
        identificador = dato_obtenido.get('identificador')
        respuesta:dict = mantenimiento.eliminar_usuario(identificador)
        return JsonResponse(respuesta)


def detalles_usuario(request,id):
    mantenimiento = MantenimientoUsuario()
    if request.method == 'GET':
        datos = mantenimiento.buscar_un_usuario(id)
        return render(request,'adminuser/administrativo/detalles_usuario.html',datos)
    


  #/obertern_usuarios/  
def obtenerUsuarios(request):
    usuarios = list(AuthUser.objects.values())
    if (len(usuarios)>0):
        datos = {
            'mensaje':'con datos',
            'usuarios':usuarios
            }
    else:
        datos = {'mensaje':'sin datos'}
    return JsonResponse(datos)
    






def opciones(request):
    return render(request, 'adminuser/reabastecimiento/reabastecimiento.html')

def proveedores(request):
    return render(request, 'adminuser/reabastecimiento/proveedores.html')

def inventariobajo(request):
    return render(request, 'adminuser/controlinventario/inventariobajo.html')


def reporte(request):
    return render(request, 'adminuser/reportes/reportes.html')

# vista para mostrar los datops


def marcas(request):
    if request.method == 'GET':
        form = MarcaForm()
        return render(request, 'adminuser/reabastecimiento/marcas.html', {'form': form})
    elif request.method == 'POST':
        form = MarcaForm(request.POST)
        respuesta = ingeso_marca(form)
        return JsonResponse(respuesta)
  
        
        
"""Vista para eliminar y acatualizar dato en espesifico"""  
def modificar_marcas(request):
    if request.method == "DELETE":
        #obteniedo los el id que nos envian en el frontend
        datos = json.loads(request.body)
        #del json obtenemos el id 
        id_marca = datos.get('id_marca')
        #procedemos a eliminarlo y devolvemos una respuesta
        respuesta = eliminar_marcas(id_marca)
    elif request.method == "PUT":
        respuesta = {'mensaje':'dato actualizado'}
    return JsonResponse(respuesta)
        
        
        
        

#def guardaMarca():
    
# vista que nos da los datos


def obtenerDatos(request):
    # creaando la lista de todas las marcas
    marcas = list(Marcas.objects.values())
    if len(marcas) > 0:
        dato = {
            'mensaje': 'Si funciono',
            'marcas': marcas
        }
    else:

        dato = {'mensaje': 'sin datos'}
    return JsonResponse(dato)


def reporteRea(request):
    return render(request, 'adminuser/reportes/reporteRea.html')



# Esto es una prueba de dashboard Bernar

def dashboard(request):
    return render(request, 'adminuser/administrativo/dashbord.html')


def adminbarra(request):
    return render(request, 'adminuser/administrativo/adminBarra.html')


# Defiendo las vista de categoria
def categorias(request):
    if request.method == 'GET':
        form = CategoriaForm()
        categorias = list(Categorias.objects.values())
        return render(request, 'adminuser/reabastecimiento/Categorias.html', {'form': form,'datos':categorias})
    elif request.method == 'POST':
        form = CategoriaForm(request.POST)
        respuesta = ingeso_marca(form)
        return JsonResponse(respuesta)
  

def obtenerDatosCategoria(request):
    # creaando la lista de todas las marcas
    categorias = list(Categorias.objects.values())
    if len(categorias) > 0:
        dato = {
            'mensaje': 'Si funciono',
            'categoria': categorias
        }
    else:

        dato = {'mensaje': 'sin datos'}
    return JsonResponse(dato)


# Definiendo las vista de Registro de Productos

def registrocompras(request):
    if request.method == 'GET':
        form = ComprasForm()
        compras = list(Compras.objects.values_list('id_compra','fecha_compra','fk_proveedor__nombre_vendedor','fk_empleado__primer_nombre','fk_metodo_pago__nombre','observaciones'))
        return render(request, 'adminuser/reabastecimiento/registroproductos.html', {'form': form,'datos':compras})
    elif request.method == 'POST':
        form = ComprasForm(request.POST)
        respuesta = ingeso_marca(form)
        return JsonResponse(respuesta)

def obtenerDatosCompras(request):
    # creaando la lista de todas las marcas
    compras = list(Compras.objects.values())
    if len(compras) > 0:
        dato = {
            'mensaje': 'Si funciono',
            'compra': compras
        }
    else:

        dato = {'mensaje': 'sin datos'}
    return JsonResponse(dato)

"""Nuevo Producto"""


def nuevo_producto(request):
    if request.method == 'GET':
        nuevoProducto=Productos.objects.values_list(
            'id_productos',
            'nombre_producto',
            'descripcion',
            'codigo_barras',
            'tamanio',
            'imagen',
            'estado',
            'fk_presentacion__nombre_presentacion',
            'fk_unidad_medida__prefijo',
            'fk_categoria__nombre_categoria',
            'fk_marca__nombre_marca'
        )
        return render(request,'adminuser/reabastecimiento/nuevoProducto.html',{'datos':nuevoProducto } )
    
        
