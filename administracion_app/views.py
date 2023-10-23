from django.shortcuts import render,redirect
#from administracion_app.models import *
""" from inicio_app.models import AuthUser """
from django.http import JsonResponse
from .formularios.fomularios_base import *
from django.views import View
from .validaciones import *
import json
from django.contrib.auth.decorators import login_required
from .models import AuthUser, Marcas


@login_required
def admon(request):
    return render(request, 'adminuser/inicio/inicio_admin.html')

""" En este apartado nosotro estamos administrando los usuarios de nuestro sistema  """

#
def administrar_usuarios(request):
    validaciones = ValidarUsuarios()
    if request.method == 'GET':
        form = UsuarioForm()
        datos:list = validaciones.obtener_datos()
        return render(request, 'adminuser/administrativo/administrativo.html', datos)

    elif request.method == 'POST':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.agregar_usuario(dato_obtenido)
        return JsonResponse(respuesta)

    elif request.method == 'DELETE':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.eliminar_usuario(dato_obtenido)
        return JsonResponse(respuesta)


def detalles_usuario(request,id):
    validaciones = ValidarUsuarios()
    if request.method == 'GET':
        datos = validaciones.buscar_usuario(id)
        return render(request,'adminuser/administrativo/detalles_usuario.html',datos)
    if request.method == 'PUT':
        datos = json.loads(request.body)
        respuesta = validaciones.actualizar_datos(datos,id)
        return JsonResponse(respuesta)
 

def opciones(request):
    return render(request, 'adminuser/reabastecimiento/reabastecimiento.html')


def inventariobajo(request):
    return render(request, 'adminuser/controlinventario/inventariobajo.html')

def reporte(request):
    return render(request, 'adminuser/reportes/reportes.html')

# vista para mostrar los datops

#-----------------------------MARCAS------------------------------------------------

def marcas(request):
    validaciones = ValidacionesMarcas()

    if request.method == 'GET':
        respuesta = validaciones.obetener_datos_marcas()
        return render(request, 'adminuser/reabastecimiento/Marcas.html', respuesta)
    
    elif request.method == 'POST':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.agregar_marcas(dato_obtenido)
        return JsonResponse(respuesta)

    elif request.method == 'DELETE':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.eliminar_marca(dato_obtenido)
        return JsonResponse(respuesta)
    elif request.method == 'PUT':
        datosJson = json.loads(request.body)
        respuesta = validaciones.actualizar_datos(datosJson)
        return JsonResponse(respuesta)
   

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




'''------------------------------------ CATEGORIA ------------------------------------------------'''

def administrar_categoria(request):
    validaciones = MantenimientoCategoria()

    if request.method == 'GET':
        respuesta = validaciones.obtener_categorias()
        return render(request, 'adminuser/reabastecimiento/Categorias.html', respuesta)

    elif request.method == 'POST':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.agregar_categorias(dato_obtenido)
        return JsonResponse(respuesta)

    elif request.method == 'DELETE':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.eliminar_categoria(dato_obtenido)
        return JsonResponse(respuesta)
    
    elif request.method == 'PUT':
        datosJson = json.loads(request.body)
        respuesta = validaciones.actualizar_datos(datosJson)
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



'''---------------Definiendo las vista de Registro de Productos --------------------'''

def registrocompras(request):
    validaciones = ValidacionesCompra()
    if request.method == 'GET':
        datos = validaciones.obtener_datos_compra()
        return render(request,'adminuser/reabastecimiento/registroproductos.html',datos)
    
    elif request.method == 'DELETE':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.eliminar_compra(dato_obtenido)
        return JsonResponse(respuesta)

    elif request.method == 'POST':
        datos = json.loads(request.body)
        respuesta = validaciones.guardar_nueva_compra(datos)
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


"""--------------------------- DETALLE COMPRA ----------------------------------------------"""

def detallecompras(request):
    if request.method == 'GET':
        form = DetalleForm()         
        detallecompras = list(DetalleCompra.objects.values_list(
            'id_detalle_compra',
            'fk_producto_id__nombre_producto',
            'fk_compra',
            'descuentos',
            'cantidad_compra',
            'precio_unitario_compra',
            'precio_sugerido_venta',
            'no_lote'
            ))
        return render(request, 'adminuser/reabastecimiento/detallecompras.html', {'form': form,'datos':detallecompras})
    elif request.method == 'POST':
        form = DetalleForm(request.POST)
        respuesta = ingeso_marca(form)
        return JsonResponse(respuesta)

def obtenerDatosDetalle(request):
    # creaando la lista de todas las marcas
    detallecompras = list(DetalleCompra.objects.values())
    if len(detallecompras) > 0:
        dato = {
            'mensaje': 'Si funciono',
            'compra': detallecompras
        }
    else:

        dato = {'mensaje': 'sin datos'}
    return JsonResponse(dato)



"""----------------------------Nuevo Producto-------------------------------------------"""
def nuevo_producto(request):
    validaciones = ValidacionesProductos()
    if request.method == 'GET':
        datos=validaciones.obtener_datos_producto()
        return render(request,'adminuser/reabastecimiento/nuevoProducto.html',datos)
    
    elif request.method == 'DELETE':
        dato_obtenido = json.loads(request.body)
        respuesta = validaciones.eliminar_producto(dato_obtenido)
        return JsonResponse(respuesta)
    
    elif request.method =='POST':
        datosJson = json.loads(request.body)
        respuesta = validaciones.guardar_nuevo_producto(datosJson)
        return JsonResponse(respuesta)
        


'''------------------------------------ Vista de Proveedores-------------------------------------'''
def proveedores(request):
    validaciones = ValidacionesProveedores()
    if request.method == 'GET':
        datos=validaciones.obtener_datos_proveedores()
        return render(request,'adminuser/reabastecimiento/proveedores.html',datos)
       
    elif request.method == 'POST':
        dato_obtenido=json.loads(request.body)
        respuesta = validaciones.agregar_proveedores(dato_obtenido)
        return JsonResponse(respuesta)

    elif request.method == 'DELETE':
        dato_obtenido=json.loads(request.body)
        respuesta = validaciones.eliminar_proveedor(dato_obtenido)
        return JsonResponse(respuesta)
    

def obtenerDatosProveedor(request):
    # creaando la lista de todas las marcas
    proveedores = list(Proveedores.objects.values())
    if len(proveedores) > 0:
        dato = {
            'mensaje': 'Si funciono',
            'proveedores': proveedores
        }
    else:

        dato = {'mensaje': 'sin datos'}
    return JsonResponse(dato)



''' -------------------------- LISTAD DE PEDIDOS ---------------------------------'''

def listadopedidos(request):
    validaciones = ValidacionListadoProductos()
    if request.method == 'GET':
        datos=validaciones.obtener_listado_producto()
        return render(request,'adminuser/reabastecimiento/listadopedido.html',datos)

    elif request.method == 'DELETE':
        dato_obtenido=json.loads(request.body)
        respuesta = validaciones.eliminar_listado(dato_obtenido)
        return JsonResponse(respuesta)
    
    elif request.method =='POST':
        datosJson = json.loads(request.body)
        respuesta = validaciones.agregar_listado(datosJson)
        return JsonResponse(respuesta)
    
    
    # if request.method == 'GET':
    #     form = listadoForm()
    #     listadopedido = list(ListadoPedidos.objects.values_list(
    #         'id_listado',
    #         'fecha_creacion',
    #         'fk_empleado_id__primer_nombre',
    #         'estado',
    #         ))
    #     return render(request, 'adminuser/reabastecimiento/listadopedido.html', {'form': form,'datos':listadopedido})
    # elif request.method == 'POST':
    #      form = ListadoPedidos(request.POST)
    #      respuesta = ingeso_marca(form)
    #      return JsonResponse(respuesta)



def obtenerDatoslistado(request):
        # creaando la lista de todas las marcas
    listadopedido = list(ListadoPedidos.objects.values())
    if len(listadopedido) > 0:
        dato = {
            'mensaje': 'Si funciono',
            'Listado de Pedido': listadopedido
        }
    else:

        dato = {'mensaje': 'sin datos'}
    return JsonResponse(dato)




#-----------------------VISTAS DE CONTROL DE MOVIMIENTO --------------------------------

def historialventas(request):
    return render(request, 'adminuser/controlinventario/historialventas.html')

def historialentradas(request):
    return render(request, 'adminuser/controlinventario/historialentradas.html')

def historialsalidas(request):
    return render(request, 'adminuser/controlinventario/historialsalidas.html')

def cardex(request):
    return render(request, 'adminuser/controlinventario/cardex.html')

def analisisgrafica(request):
    return render(request, 'adminuser/controlinventario/analisisgrafica.html')


    #---------------BALANCE DE CAJA----------------------------
def agregaregreso(request):
    return render(request, 'adminuser/controlinventario/agregaregresos.html')

def agregaringreso(request):
    return render(request, 'adminuser/controlinventario/agregaringreso.html')

def balancecaja(request):
    return render(request, 'adminuser/controlinventario/balancecaja.html')

def informeanalisis(request):
    return render(request, 'adminuser/controlinventario/informeanalisis.html')

#---------------MODAL ACTUALIZACION NUEVO PRODUCTO----------------------------

def modalactualizacion(request,id):
    validaciones = ValidacionesProductos()
    if request.method == 'GET':
        datos = validaciones.buscar_producto(id)
        return render(request, 'adminuser/reabastecimiento/modalactualizacion.html',datos)
    if request.method == 'PUT':
        datos = json.loads(request.body)
        respuesta = validaciones.actualizar_datos(datos,id)
        return JsonResponse(respuesta)