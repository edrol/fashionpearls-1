from django.db import models
from common.models import Person


class Provider(Person):
    address = models.CharField('fiscal address', max_length=40, null=True)

    class Meta:
        verbose_name = 'provider'
        verbose_name_plural = 'providers'

# Create your models here.
