#from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('adm/',views.administrador, name='adm'),
    path('login/',views.login, name='login')
]
