from .models import Marcas
# los objetos, listas y dicionarios se pasan por referencia y no por valor
# las variables simples se se pasan por valor osea por copia
from .models import *
from django.contrib.auth.models import User
import json
from .mantenimiento import MantenimientoGeneral
from django.utils import timezone
import sys
from .formularios.fomularios_base import *

"""funcion que me permite obtener datos del formularios de ingreso de datos"""


def obtener_datos_marca(form) -> dict:
    datos: dict = {}
    datos['nombre_marca'] = form.cleaned_data['nombremarca']
    datos['descripcion'] = form.cleaned_data['descripcion']
    datos['estado'] = form.cleaned_data['estado']
    return datos


"""Gurdamos una nueva marca en nuestra tabla marcas"""


def guardar_nueva_marca(datos: dict):
    nueva_marca = Marcas(
        nombre_marca=datos['nombre_marca'],
        estado=datos['estado'],
        descripcion=datos['descripcion']
    )
    nueva_marca.save()
    datos['id_marcas'] = nueva_marca.id_marcas
    datos['mensaje'] = 'Dato guardado exitosamente'
    datos['condicion']= 'ok'



def validacion_duplicado(nom_marca):
    existencia = Marcas.objects.filter(nombre_marca=nom_marca).exists()
    print(existencia)
    return existencia



""" Funcion del proceso de registro de una nueva marca """
def ingeso_marca(form) -> dict:
    datos ={}
    if form.is_valid():
        datos = obtener_datos_marca(form)
        print(datos['nombre_marca'])
        if not(validacion_duplicado(datos['nombre_marca'])):
            guardar_nueva_marca(datos)
        else:
            datos['mensaje'] = 'Datos duplicado'
            datos['condicion']= 'error'
    else:
        datos['mensaje'] = 'Se encontraron problemas por favor comuniquese con el inge Abi'
        datos['condicion']= 'error'
    return datos




"""Eliminar marcas"""
def eliminar_marcas(_id_marca:int):
    try:
        marca_eliminar = Marcas.objects.get(id_marcas= _id_marca)
        marca_eliminar.delete()
        return {'mensaje':'Dato Eliminado'}
    except marca_eliminar.DoesNotExist:
        print('No se encontro el dato')
        return {'mensaje':'Dato no econtrado'}
    except Exception as error:
        print(f'erro al eliminar {error}')
        return {'mensaje':'Error'}


"""--------------para otros----------------"""

# datos categoria
# def obtener_datos_categoria(form) -> dict:
#     datos: dict = {}
#     datos['nombre_categoria'] = form.cleaned_data['nombrecategoria']
#     datos['descripcion'] = form.cleaned_data['descripcion']
#     datos['estado'] = form.cleaned_data['estado']
#     return datos


# #Datos compras
# def obtener_datos_compras(form) -> dict:
#     datos: dict = {}
#     datos['fecha_compra'] = form.cleaned_data['nombrecompra']
#     datos['fk_proveedor'] = form.cleaned_data['proveedor']
#     datos['fk_empleado'] = form.cleaned_data['empleado']
#     datos['fk_metodo_pago'] = form.cleaned_data['metodopago']
#     datos['observaciones'] = form.cleaned_data['observaciones']
#     return datos



#NUEVA CLASE GENERAL Mantenimiento




#-----------------------------------------------------------
class ValidarUsuarios:
    _mantenimiento = MantenimientoGeneral(AuthUser)
    def actualizar_datos(self,datos,id):
        actualizacion = {}
        if 'password' in datos:
            usuario = User.objects.get(id=id)
            usuario.set_password(datos.pop('password'))
            usuario.save()
        filtro = {'id': id}
        actualizacion:dict = self._mantenimiento.actualizar_registro(datos,filtro)
        actualizacion['datos']['is_active'] = 'Si' if actualizacion['datos']['is_active'] else 'No'
        actualizacion['datos']['is_superuser'] = 'Si' if actualizacion['datos']['is_superuser'] else 'No'
        return actualizacion
        
    def buscar_usuario(self,id):
        filtro = {'id':id}  
        dato = self._mantenimiento.buscar_registros(filtro)
        return {'usuario':dato}
    
    def agregar_usuario(self,datosJson):
        try:
            respuesta = {}
            validacion = ['username']
            datosJson['is_staff'] = False
            datosJson['date_joined'] = timezone.now()
            respuesta = self._mantenimiento.agregar_registro(datosJson,'id',validacion)
            if respuesta['condicion'] == 'ok':
                print("------antes-------")
                print(respuesta) 
                usuario = User.objects.get(id=respuesta['datos']['id'])
                print("------antes del final-------")
                print(datosJson)
                usuario.set_password(respuesta['datos'].pop('password'))
                usuario.save()
                print("------final-------")
                print(respuesta)
            return respuesta
        except Exception as error:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print(f"Tipo de excepción: {exc_type}")
            print(f"Mensaje de excepción: {exc_value}")
            print(f"Ubicación del error: {exc_traceback.tb_frame.f_code.co_filename}, línea {exc_traceback.tb_lineno}")
            return {'mensaje':'Error fatal datos equivocados', 'condicion':'error' }
        
    def obtener_datos(self):
        form = UsuarioForm()
        datos = self._mantenimiento.obtener_datos()
        return {
            'form': form,
            'datos':datos
        }
        
    def eliminar_usuario(self,dato):
        try:
            identificador = {'id': int(dato.get('identificador'))}
            respuesta = self._mantenimiento.eliminar_registro(identificador)
            print(respuesta)
            if respuesta['condicion'] == 'ok':
                respuesta['mensaje'] = 'El usuario se ha eliminado correctamente'
            return respuesta
        except:
            return {'mensaje':'Error fatal datos equivocados', 'condicion':'error' }
        


class ValidarProductos():
    _mantenimiento = MantenimientoGeneral(Productos)
    def eliminar_producto(self,dato):
        try:
            identificador = {'id': int(dato.get('identificador'))}
            respuesta = self._mantenimiento.eliminar_registro(identificador)
            print(respuesta)
            if respuesta['condicion'] == 'ok':
                respuesta['mensaje'] = 'El usuario se ha eliminado correctamente'
            return respuesta
        
        except:
            return {'mensaje':'Error fatal datos equivocados', 'condicion':'error' }
        
        


#------------------------------ CATEGORIAS -----------------------------------

class MantenimientoCategoria():
    _mantenimiento = MantenimientoGeneral(Categorias)
    def obtener_categorias(self) -> dict:
        form = CategoriaForm()
        datos = self._mantenimiento.obtener_datos()
        return {
            'form': form,
            'datos':datos
        }
    
    def agregar_categorias(self, datos):
        validacion = ['nombre_categoria']
        respuesta = self._mantenimiento.agregar_registro(datos,'id_categoria',validacion)
        return respuesta
        

    def eliminar_categoria(self,datos):
        respuesta = self._mantenimiento.eliminar_registro({'id_categoria':int(datos['identificador'])})
        print(respuesta)
        if respuesta['condicion'] == 'ok':
            respuesta['mensaje'] = 'La categoria se ha eliminado correctamente'
        return respuesta
    
    def actualizar_datos(self,datosJs:dict):
        filtro = {'id_categoria':datosJs.pop('identificador')}
        actualizacion = self._mantenimiento.actualizar_registro(datosJs,filtro)
        if actualizacion['condicion'] == 'ok':
            actualizacion['datos']['estado'] = 'Activo' if actualizacion['datos']['estado'] else 'Inactivo'
        return actualizacion


#----------------------------------CATALOGO DE PRODUCTOS---------------------------------
   
class ValidacionesProductos:
    _mantenimiento=MantenimientoGeneral(Productos)
       #OBTENER DATOS  
        #metodo
    def obtener_datos_producto(self):
        filtro=[
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
        ]
        respuesta=self._mantenimiento.obtener_datos_especificos(filtro)
        form=NuevoProducto()
        return {
            'form':form,
            'datos':respuesta,
            
        }
    def guardar_producto(self,req_post):
        formulario = NuevoProducto(req_post)
        datos = self._mantenimiento.agregar_registro_baseForm(formulario)
        print(datos)
        return datos
    #GUARDAR NUEVO PRODUCTO
    def guardar_nuevo_producto(self,datosJson):
        datosJson['fk_presentacion'] = Presentacion.objects.get(id_presentacion = datosJson['fk_presentacion'])
        datosJson['fk_unidad_medida']= UnidadesMedidas.objects.get(id_medicion = datosJson['fk_unidad_medida'])
        datosJson['fk_categoria'] = Categorias.objects.get(id_categoria = datosJson['fk_categoria'])        
        datosJson['fk_marca'] = Marcas.objects.get(id_marcas = datosJson['fk_marca'])
        print(datosJson)
        resultado = self._mantenimiento.agregar_registro(datosJson,'id_productos',['nombre_producto'])
        resultado['datos']['fk_presentacion'] =  datosJson['fk_presentacion'].pk
        resultado['datos']['fk_unidad_medida'] = datosJson['fk_unidad_medida'].pk 
        resultado['datos']['fk_categoria'] = datosJson['fk_categoria'].nombre_categoria 
        resultado['datos']['fk_marca'] = datosJson['fk_marca'].pk 
        print(resultado)
        return resultado

    def eliminar_producto(self,datosJson):
        try:
            respuesta = self._mantenimiento.eliminar_registro({'id_productos':int(datosJson['identificador'])})
            print(respuesta)
            if respuesta['condicion'] == 'ok':
                respuesta['mensaje'] = 'El producto se ha eliminado correctamente'
            return respuesta
        except:
            return {'mensaje':'Error fatal datos equivocados', 'condicion':'error' }
          
    def buscar_producto(self,id):
        form=NuevoProducto()
        filtro = {'id_productos':id}  
        dato = self._mantenimiento.buscar_registros(filtro)
        return {
            'producto':dato,
            'form':form
            }
            
        

"""----------------------------------MARCAS---------------------------------"""

class ValidacionesMarcas:
    _mantenimiento = MantenimientoGeneral(Marcas)
    def obetener_datos_marcas(self) -> dict:
        form = MarcaForm()
        datos = self._mantenimiento.obtener_datos()
        return {
            'form': form,
            'datos':datos
        }
    def agregar_marcas(self, datos):
        validacion = ['nombre_marca']
        respuesta = self._mantenimiento.agregar_registro(datos,'id_marcas',validacion)
        return respuesta
    
    def eliminar_marca(self,datos):
        respuesta = self._mantenimiento.eliminar_registro({'id_marcas':int(datos['identificador'])})
        print(respuesta)
        if respuesta['condicion'] == 'ok':
            respuesta['mensaje'] = 'La marca se ha eliminado correctamente'
        return respuesta
    
    def actualizar_datos(self,datosJs:dict):
        filtro = {'id_marcas':datosJs.pop('identificador')}
        actualizacion = self._mantenimiento.actualizar_registro(datosJs,filtro)
        if actualizacion['condicion'] == 'ok':
            actualizacion['datos']['estado'] = 'Activo' if actualizacion['datos']['estado'] else 'Inactivo'
        return actualizacion




"""------------------------------ PROVEEDORES -----------------------------------"""

class ValidacionesProveedores:
    _mantenimiento = MantenimientoGeneral(Proveedores)
    def obtener_datos_proveedores(self) -> dict:
        form = ProveedoresForm()
        datos = self._mantenimiento.obtener_datos()
        return {
            'form': form,
            'datos':datos
        }
    def agregar_proveedores(self, datos):
        validacion = ['nombre_vendedor']
        respuesta = self._mantenimiento.agregar_registro(datos,'id_proveedor',validacion)
        return respuesta

    def eliminar_proveedor(self,datos):
        respuesta = self._mantenimiento.eliminar_registro({'id_proveedor':int(datos['identificador'])})
        print(respuesta)
        if respuesta['condicion'] == 'ok':
            respuesta['mensaje'] = 'El proveedor se ha eliminado correctamente'
        return respuesta


'''------------------------------ LISTADO PRODUCTOS ------------------------------'''

class ValidacionListadoProductos():
    _mantenimiento = MantenimientoGeneral(ListadoPedidos)
    def obtener_listado(self) -> dict:
        form = listadoForm()
        datos = self._mantenimiento.obtener_datos()
        return {
            'form': form,
            'datos':datos
        }
    
    
    def obtener_listado_producto(self):
        filtro=[
            'id_listado',
            'fecha_creacion',
            'fk_empleado__primer_nombre',
            'estado',
        ]
        respuesta=self._mantenimiento.obtener_datos_especificos(filtro)
        form = listadoForm()
        return {
            'form':form,
            'datos':respuesta,
        }
        
    def guardar_listado(self,req_post):
        formulario = listadoForm(req_post)
        datos = self._mantenimiento.agregar_registro_baseForm(formulario)
        print(datos)
        return datos


    def agregar_listado(self, datosJson):
        datosJson['fk_empleado'] = Empleados.objects.get(id_empleado = datosJson['fk_empleado'])
        print(datosJson)
        # validacion = ['']
        respuesta = self._mantenimiento.agregar_registro(datosJson,'id_listado')
        respuesta['datos']['fk_empleado'] = datosJson['fk_empleado'].primer_nombre
        print(respuesta)
        return respuesta

    def eliminar_listado(self,datos):
        respuesta = self._mantenimiento.eliminar_registro({'id_listado':int(datos['identificador'])})
        print(respuesta)
        if respuesta['condicion'] == 'ok':
            respuesta['mensaje'] = 'El listado se ha eliminado correctamente'
        return respuesta



'''------------------------------ COMPRAS -----------------------------------'''

class   ValidacionesCompra:
    _mantenimiento = MantenimientoGeneral(Compras)
    def obtener_datos_compra(self):
        filtro=[
            'id_compra',
            'fecha_compra',
            'fk_proveedor__nombre_vendedor',
            'fk_empleado__primer_nombre',
            'fk_metodo_pago__nombre',
            'observaciones'
        ]
        respuesta=self._mantenimiento.obtener_datos_especificos(filtro)
        form=Comprasform()
        return {
            'form':form,
            'datos':respuesta,
            
        }
        
    def guardar_compra(self,req_post):
        formulario = Comprasform(req_post)
        datos = self._mantenimiento.agregar_registro_baseForm(formulario)
        print(datos)
        return datos

    #GUARDAR NUEVA COMPRA
    def guardar_nueva_compra(self,datosJson):
        datosJson['fk_proveedor'] = Proveedores.objects.get(id_proveedor = datosJson['fk_proveedor'])
        datosJson['fk_empleado']= Empleados.objects.get(id_empleado = datosJson['fk_empleado'])
        datosJson['fk_metodo_pago'] = MetodosPago.objects.get(id_metodo_pago = datosJson['fk_metodo_pago'])        
        print(datosJson)
        resultado = self._mantenimiento.agregar_registro(datosJson,'id_compra')
        resultado['datos']['fk_proveedor'] =  datosJson['fk_proveedor'].nombre_vendedor
        resultado['datos']['fk_empleado'] = datosJson['fk_empleado'].primer_nombre
        resultado['datos']['fk_metodo_pago'] = datosJson['fk_metodo_pago'].nombre

        print(resultado)
        return resultado

    def eliminar_compra(self,datosJson):
        try:
            respuesta = self._mantenimiento.eliminar_registro({'id_compra':int(datosJson['identificador'])})
            print(respuesta)
            if respuesta['condicion'] == 'ok':
                respuesta['mensaje'] = 'La compra se ha eliminado correctamente'
            return respuesta
        except:
            return {'mensaje':'Error fatal datos equivocados', 'condicion':'error' }
          
    def buscar_compra(self,id):
        form=Comprasform()
        filtro = {'id_compra':id}            
        dato = self._mantenimiento.buscar_registros(filtro)
        return {
            'compra':dato,
            'form':form
            }