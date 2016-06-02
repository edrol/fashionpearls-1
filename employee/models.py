from django.db import models
from common.models import Person

class Employee(Person):
    salary = models.DecimalField('salary', max_digits=7, decimal_places=2, default=0000.00)

    def __unicode__(self):
        return '%s %s' % (self.name, self.last_name)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
# Create your models here.
