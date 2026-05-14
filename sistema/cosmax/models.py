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