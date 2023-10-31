from django.urls import path
from . import views

#/usuario-vetas/....
urlpatterns = [
    #path('',views.admon, name='panel_principal'),
   

     path('registrar-venta/',views.registrarventa, name='registrar_venta'),
     path('productos-agotados/',views.productosagotados, name='productos_agotados'),
     path('comprobante/',views.comprobante, name='comprobante'),
     path('obtener-datos-inventario/<int:id>/',views.api_ventas, name='api_inventario'),
     
]