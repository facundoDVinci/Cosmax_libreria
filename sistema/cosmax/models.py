from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    ADMIN = 'admin'
    EMPLEADO = 'empleado'

    ROLES = [
        (ADMIN, 'Administrador'),
        (EMPLEADO, 'Empleado')
    ]

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default=EMPLEADO
    )

    def es_admin(self):
        return self.rol == self.ADMIN

    def es_empleado(self):
        return self.rol == self.EMPLEADO
    
class Libro(models.Model):

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo

class Cliente(models.Model):

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Venta(models.Model):

    METODOS_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia')
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    empleado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    fecha = models.DateTimeField(auto_now_add=True)

    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO, default='EFECTIVO')

    def __str__(self):

        return f"Venta #{self.id}"
    
class DetalleVenta(models.Model):

    venta = models.ForeignKey(
        Venta,
        on_delete=models.CASCADE
    )

    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE
    )

    cantidad = models.PositiveIntegerField(default=1)

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return f"{self.libro.titulo}"
   

