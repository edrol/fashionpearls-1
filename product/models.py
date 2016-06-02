from django.db import models
from provider.models import Provider

ACTIVATE = (
    ('1', 'active'),
    ('0', 'inactive'),
)

class Category(models.Model):
    name = models.CharField('name', max_length=50)

    def __unicode__(self):
        return '%s' % (self.name )

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    code = models.CharField('product code',max_length=15,unique=True)
    name = models.CharField('product name', max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True)
    cost = models.DecimalField('cost price', max_digits=5, decimal_places=2, default=0.00)
    sale = models.DecimalField('sale price', max_digits=5, decimal_places=2, default=0.00)
    quantity = models.PositiveSmallIntegerField()
    active = models.CharField('active', max_length=1, choices=ACTIVATE, default='1')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def price_total(self):
        precio_total = self.cost*self.quantity
        return precio_total