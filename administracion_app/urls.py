from django.urls import path
from . import views


urlpatterns = [
     path('',views.admon, name='panel_principal'),
     path('gestion-usuarios/',views.administrar_usuarios,name='gestion_usuarios'),
     path('detalles-usuario/<int:id>/',views.detalles_usuario,name='detalles_usuario'),
     path('panel-reabastecimiento/',views.opciones, name='reabastecimiento'),   
     path('reporte/',views.reporte, name='reportes'),
     path('ingreso-marcas/',views.marcas, name='marcas'),
     path('rep-reabastecimiento/',views.reporteRea, name='reporte_reabastecimiento'),
     path('obtener-marcas/',views.obtenerDatos,name='obtener_marcas'),
     path('obtener-usuario/',views.obtenerUsuarios, name="obtener_usuario"),
     # prueba dashboard
     path('bernar/',views.dashboard,  name='dashboard'),#
     path('modifica-marcas/',views.modificar_marcas,name='modificar_marcas'),
     path('proveedores/',views.proveedores, name='proveedores'),
     path('obtener-proveedores/',views.obtenerDatosProveedor, name='obtener_proveedores'),
     path('inventario-bajo/',views.inventariobajo, name='inventariobajo'),
      path('adminbarra/',views.adminbarra,  name='adminbarra'),#

      # Categorias 
      path('categorias/',views.categorias, name='categorias'),
      path('obtener_categorias/',views.obtenerDatosCategoria,name='obtener_categorias'),
      
      #Compras
      path('compras/',views.registrocompras, name='compras'),
      path('obtener-compras/',views.obtenerDatosCompras,name='obtener_compras'),
      #detalle compras
      path('detalle-compras/',views.detallecompras, name='detalle_compras'),
      path('obtener-detalle-compras/',views.obtenerDatosDetalle,name='obtener_detalle_compras'),
     
      #Listado de Pididos
      path('listado-pedidos/',views.listadopedidos, name='listadopedidos'),
      path('obtener-listado/',views.obtenerDatoslistado,name='obtener_pedidos'),
      #Ingreso-producto_
      path('ingreso-productos/',views.nuevo_producto, name='productos_nuevos')
]


