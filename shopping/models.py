from django.db import models
from django.db.models import signals
from provider.models import Provider
from product.models import Product

class Buy(models.Model):
    code = models.CharField('code', max_length=10, null=True)
    provider = models.ForeignKey(Provider)
    date = models.DateTimeField('date', auto_now_add=True)
    product = models.ManyToManyField(Product, through='Purchase_Detail')

    def __unicode__(self):
        return self.code

    class Meta:
        verbose_name = 'buy'
        verbose_name_plural = 'shopping'

class Purchase_Detail(models.Model):
    buy = models.ForeignKey(Buy)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(null=False)

    #def __unicode__(self):
       #return self.buy.code

    class Meta:
        verbose_name = 'purchase detail'
        verbose_name_plural = 'Details shopping'


def update_stock(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()


signals.post_save.connect(update_stock, sender=Purchase_Detail, dispatch_uid="update_stock_count")
# Create your models here.
