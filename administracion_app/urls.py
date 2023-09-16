from django.urls import path, include
from . import views

urlpatterns = [
     path('patito/',views.patito, name='inicio_admin'),
     path('panel/',views.adminpanel,name='panel'),
     path('raton/',views.raton, name='abastecimiento'),
]
