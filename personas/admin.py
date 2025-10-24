from django.contrib import admin

# Register your models here.
from .models import Persona

admin.site.register(Persona)
admin.site.site_header = "Sistema de Gestión de Personas"
admin.site.site_title = "Gestión de Personas"
admin.site.index_title = "Panel de Administración"
