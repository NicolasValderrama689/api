from django.contrib import admin
from .models import programmer

# Register your models here.
# Aqui se crean los modelos (las tablas o colecciones)
admin.site.register(programmer)#se registra el modelo para poder verlosen el panel de administracion 
