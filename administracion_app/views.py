from django.shortcuts import render,redirect
from administracion_app.models import *
from django.http import JsonResponse
from .formularios.fomularios_base import MarcaForm
from .formularios.fomularios_base import CategoriaForm
from .validaciones import ingeso_marca,eliminar_marcas
import json 

def admon(request):

    return render(request, 'adminuser/inicio/inicio_admin.html')

""" En este apartado nosotro estamos administrando los usuarios de nuestro sistema  """

def administar_usuario(request):
    if request.method == 'GET':
        usuarios:AuthUser = list(AuthUser.objects.values_list('id','first_name','username','is_superuser'))
        return render(request, 'adminuser/administrativo/administrativo.html', {'usuarios':usuarios})
    elif request.method == 'POST':
        form = MarcaForm(request.POST)
        respuesta:dict = ingeso_marca(form)
        return JsonResponse(respuesta)



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

def inventariosbajos(request):
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
        datos = json.loads(request.body)
        id_marca = datos.get('id_marca')
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
        return render(request, 'adminuser/reabastecimiento/Categorias.html', {'form': form})
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