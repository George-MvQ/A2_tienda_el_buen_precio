from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .form_users import LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.


def inicio(request):
    return render(request, 'index.html')


def administrador(request):
    return render(request, 'infoTienda.html')



def logeo(request):
    if request.method =='GET':
        print('111')
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    else: 
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            user = authenticate(request, username=username, password=password)
            print(user is not None)
            if user is not None and user.check_password(password):
                login(request, user)
                if user.is_superuser:
                    print('1')
                    return redirect('/admin/')
                else:
                   print('2')
                   return HttpResponse('<h1>Este es un usuario Normal :)</h1>')
            else:
                return HttpResponse('j')
        else:
            return redirect('/')
            
        


def prueba(request):
    datos = {
        'titulo': 'este es una prueba',
        'contenido':'este es el contenido',
        'form': UserCreationForm
    }
    return render(request, 'pruebas.html', datos)
