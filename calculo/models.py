from django.db import models
from employee.models import Employee


class Movimiento(models.Model):
    cantidad = models.DecimalField(max_digits = 10 , decimal_places = 2)
    precio = models.DecimalField(max_digits = 10 , decimal_places = 2)
    #comision = models.DecimalField(max_digits = 10 , decimal_places = 2)

    def Total_Venta(self):
        total = (self.cantidad*self.precio)
        return total


# Create your models here.
