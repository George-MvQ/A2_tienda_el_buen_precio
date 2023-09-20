from django.shortcuts import render
from  administracion_app.models import *
from django.http import JsonResponse

def admon(request):
    return render(request, 'adminuser/inicio/inicio_admin.html')

def adminpanel(request):
    return render(request, 'adminuser/administrativo/administrativo.html')

def opciones(request):
    return render(request, 'adminuser/reabastecimiento/reabastecimiento.html')

def reporte(request):
    return render(request, 'adminuser/reportes/reportes.html')

#vista para mostrar los datops 
def marcas(request):
    return render(request, 'adminuser/reabastecimiento/marcas.html')

#vista que nos da los datos
def obtenerDatos(request):
    #creaando la lista de todas las marcas
    marcas = list( Marcas.objects.values() )
    if len(marcas)>0:
        print(marcas)
        dato = {
            'mensaje':'Si funciono',
            'marcas':marcas
        }
    else:

        dato = {'mensaje':'sin datos'}
    return JsonResponse(dato)
    

def reporteRea(request):
    return render(request, 'adminuser/reportes/reporteRea.html')

