from django.shortcuts import render

def patito(request):
    return render(request, 'adminuser/inicio/inicio_admin.html')


def adminpanel(request):
    return render(request, 'adminuser/administrativo/administrativo.html')

def raton(request):
    return render(request, 'adminuser/reabastecimiento/reabastecimiento.html')


