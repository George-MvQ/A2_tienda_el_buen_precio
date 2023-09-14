from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'index.html')

def administrador(request):
    return render (request, 'infoTienda.html')

def login(request):
    return render (request, 'login.html')