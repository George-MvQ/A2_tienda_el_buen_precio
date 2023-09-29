from django.urls import path
from . import views

urlpatterns = [
     path('admon/',views.admon, name='inicio_admin'),
     path('panel/',views.administar_usuario,name='panel'),
     path('opciones/',views.opciones, name='reabastecimiento'),
     path('reporte/',views.reporte, name='reportes'),
     path('ingresomarcas/',views.marcas, name='marcas'),
     path('reporteRea/',views.reporteRea, name='reporte_reabastecimiento'),
     path('obtener_marcas/',views.obtenerDatos,name='obtener_marcas'),
     path('obtener_usuario/',views.obtenerUsuarios, name="obtener_usuario"),
     # prueba dashboard
     path('bernar/',views.dashboard,  name='dashboard'),
     path('modifica-marcas/',views.modificar_marcas,name='modificar_marcas'),
     path('proveedores/',views.proveedores, name='proveedores'),
     path('inventariobajo/',views.inventariobajo, name='inventariobajo'),



      path('adminbarra/',views.adminbarra,  name='adminbarra'),

      # Categorias

      path('ingresocategorias/',views.categorias, name='categorias'),
      path('obtener_categorias/',views.obtenerDatosCategoria,name='obtener_categorias')
      #registro Producto
]


