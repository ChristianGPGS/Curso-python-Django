from clientes.models import Clientes, Coche
from django.contrib import admin
from webapp.models import Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Clientes)
admin.site.register(Coche)
