from django.shortcuts import render
from django.http import JsonResponse

from .validaciones import *
# Create your views here.


#------------------------VENTAS--------------------------------
def registrarventa(request):
    validaciones = ValidacionVenta()
    if request.method == 'GET':
        datos = validaciones.obtener_venta()
        return render(request, 'registrar_venta.html',datos)

def api_ventas(request, id):
    validaciones = ValidarDatosVentas()
    if request.method == 'GET':
        datos = validaciones.obtener_datos_inventario(id)
        return JsonResponse(datos)

    
    pass

def productosagotados(request):
    return render(request, 'productos_agotados.html')

def comprobante(request):
    return render(request, 'comprobante.html')


