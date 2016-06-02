from django.db import models
from common.models import Person

class Customer(Person):
    email = models.EmailField(null=True)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
# Create your models here.
