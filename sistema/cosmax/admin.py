from django.contrib import admin
from .models import Usuario, Libro, Cliente

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Cliente)