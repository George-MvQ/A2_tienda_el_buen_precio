from django.contrib import admin
from inicio_app.models import Empleados,Proveedores, Puestos,Marcas,Compras,MetodosPago,Productos,Presentacion, UnidadesMedidas
# Register your models here.
admin.site.register(Marcas)
admin.site.register(Empleados)
admin.site.register(Puestos)
admin.site.register(Proveedores)
admin.site.register(Compras)
admin.site.register(MetodosPago)
admin.site.register(Productos)
admin.site.register(Presentacion)
admin.site.register( UnidadesMedidas)

admin.site.login_template = 'admin/login.html'