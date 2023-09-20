from django.urls import path, include
from . import views

urlpatterns = [
     path('admon/',views.admon, name='inicio_admin'),
     path('panel/',views.adminpanel,name='panel'),
     path('opciones/',views.opciones, name='reabastecimiento'),
     path('reporte/',views.reporte, name='reportes'),
     path('ingresomarcas/',views.marcas, name='marcas'),
     path('reporteRea/',views.reporteRea, name='reporte_reabastecimiento'),
     path('obtener_marcas/',views.obtenerDatos,name='obtener_marcas'),
]

