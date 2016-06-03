from django.db import models
from django.db.models import signals
from employee.models import Employee
from product.models import Product
from customer.models import Customer


class Sale_S(models.Model):
    invoice = models.CharField('invoice', max_length=10, null=True)
    customer = models.ForeignKey(Customer)
    employee = models.ForeignKey(Employee)
    date = models.DateTimeField('date', auto_now_add=True)
    product = models.ManyToManyField(Product, through='Sales_Detail')

    def __unicode__(self):
        return self.invoice

    class Meta:
        verbose_name = 'sale'
        verbose_name_plural = 'sales'


class Sales_Detail(models.Model):
    sale = models.ForeignKey(Sale_S)
    product = models.ForeignKey(Product, null=True)
    quantity = models.IntegerField(null=False)

    def __unicode__(self):
        return self.sale.invoice

    def sub_total(self):
        subTotal = (self.quantity * self.product.sale)
        return subTotal

    class Meta:
        verbose_name = 'details sale'
        verbose_name_plural = 'details sales'


def update_stock(sender, instance, **kwargs):
    instance.product.quantity -= instance.quantity
    instance.product.save()


signals.post_save.connect(update_stock, sender=Sales_Detail, dispatch_uid="update_stock_count")
