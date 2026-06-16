from django.contrib import admin
from .models.models import Usuario, Libro, Cliente, Venta, DetalleVenta

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(DetalleVenta)