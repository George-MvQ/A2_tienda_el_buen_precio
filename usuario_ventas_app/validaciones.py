from .models import *
import json

from .formularios import *


import sys
from .mantenimiento import MantenimientoGeneral




class ValidacionVenta:
    _manteninimiento = MantenimientoGeneral(Inventario)
    def obtener_venta(self) -> dict: 
        form = Ventasform()
        #datos = self._manteninimiento.obtener_datos()
        return {
            #'datos': datos,
            'form': form
        }
    
    
class ValidarDatosVentas:
    _mantenimiento = MantenimientoGeneral(Inventario)
    def obtener_datos_inventario(self,id):
        producto = self._mantenimiento.buscar_registros({'id_inventario':id})
        return {
            'total_stock': producto.total_stock,
            'precio_venta': float(producto.precio_venta)
        }


