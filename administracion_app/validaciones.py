from .models import Marcas
# los objetos, listas y dicionarios se pasan por referencia y no por valor
# las variables simples se se pasan por valor osea por copia
from .models import *

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
    datos['mensaje'] = 'bien'



""" Funcion del proceso de registro de una nueva marca """
def ingeso_marca(form) -> dict:
    if form.is_valid():
        datos = obtener_datos_marca(form)
        guardar_nueva_marca(datos)
    else:
        datos['mensaje'] = 'Error'
        print("sin datos")
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
def obtener_datos_categoria(form) -> dict:
    datos: dict = {}
    datos['nombre_categoria'] = form.cleaned_data['nombrecategoria']
    datos['descripcion'] = form.cleaned_data['descripcion']
    datos['estado'] = form.cleaned_data['estado']
    return datos


#Datos compras
def obtener_datos_compras(form) -> dict:
    datos: dict = {}
    datos['fecha_compra'] = form.cleaned_data['nombrecompra']
    datos['fk_proveedor'] = form.cleaned_data['proveedor']
    datos['fk_empleado'] = form.cleaned_data['empleado']
    datos['fk_metodo_pago'] = form.cleaned_data['metodopago']
    datos['observaciones'] = form.cleaned_data['observaciones']
    return datos


#----------Usuarios------------
class MantenimientoUsuario():
    def obtener_usuarios(self):
        usuarios:list = list(AuthUser.objects.values_list('id','username','email','is_superuser'))
        return usuarios
    
    def buscar_un_usuario(self,identificador:int):
        try:
            usuario = AuthUser.objects.get(id=identificador)
            dato = {"usuario":usuario}
            return dato
        except AuthUser.DoesNotExist:
            print("no existe usuario")
            return {"mensaje":"error"}
            
    """Un ejemplo de actualizacion 
    
    def actualizar_usuario(self, id_usuario: int, nuevos_datos: dict):
    try:
        usuario_actualizar = AuthUser.objects.get(id=id_usuario)
        
        # Actualiza los campos del usuario con los nuevos datos proporcionados
        for clave, valor in nuevos_datos.items():
            setattr(usuario_actualizar, clave, valor)
        
        # Guarda los cambios en la base de datos
        usuario_actualizar.save()
        
        return {'mensaje': 'El usuario se ha actualizado correctamente!'}
    
    except AuthUser.DoesNotExist:
        print('No se encontró el usuario')
        return {'mensaje': 'Usuario no encontrado'}
    
    except Exception as error:
        print(f'Error al actualizar el usuario: {error}')
        return {'mensaje': 'Error'}
    """


    def eliminar_usuario(self, id_usuario:int):
        try:
            usuario_eliminar = AuthUser.objects.get(id = id_usuario)
            usuario_eliminar.delete()
            return {'mensaje':'El usuario se ha eliminado correctamente!'}
        except usuario_eliminar.DoesNotExist:
            print('No se encontro el dato')
            return {'mensaje':'Dato no econtrado'}
        except Exception as error:
            print(f'erro al eliminar {error}')
            return {'mensaje':'Error'}
    
    


