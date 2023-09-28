from django.contrib import admin
from inicio_app.models import Empleados,Proveedores, Puestos,Marcas
# Register your models here.
admin.site.register(Marcas)
admin.site.register(Empleados)
admin.site.register(Puestos)
admin.site.register(Proveedores)

admin.site.login_template = 'admin/login.html'