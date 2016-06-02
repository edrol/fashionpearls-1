from django.db import models


GENDER = {
    ('F','Female'),
    ('M','Male'),
    ('-','Others')
}

class Person(models.Model):
    nit = models.CharField('NIT o DPI', max_length=10, unique=True, primary_key=True)
    name = models.CharField('name', max_length=20, null=True)
    last_name = models.CharField('last name', max_length=20, null=True)
    #business_name = models.CharField('business name', max_length=50, null=True, blank=True)
    gender = models.CharField('gender', max_length=1, choices=GENDER, default='-')
    birthday = models.DateField('birthday', null=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.last_name)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'people'

class Address(models.Model):
    description = models.CharField('address', max_length=40)
    address = models.ForeignKey(Person, null=True, blank=True)

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

class Phone(models.Model):
    number = models.CharField('phone', max_length=10, null=True)
    phone = models.ForeignKey(Person, null=True, blank=True)

    def __unicode__(self):
        return self.number

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'
# Create your models here.
