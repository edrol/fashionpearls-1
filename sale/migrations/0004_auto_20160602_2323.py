# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_email'),
        ('product', '0002_auto_20160525_1958'),
        ('employee', '0001_initial'),
        ('sale', '0003_sale_sales_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale_S',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invoice', models.CharField(max_length=10, null=True, verbose_name=b'invoice')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'date')),
                ('custom', models.ForeignKey(to='customer.Customer')),
                ('employ', models.ForeignKey(to='employee.Employee')),
            ],
            options={
                'verbose_name': 'sale',
                'verbose_name_plural': 'sales',
            },
        ),
        migrations.RemoveField(
            model_name='sale',
            name='custom',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='employ',
        ),
        migrations.AlterField(
            model_name='sales_detail',
            name='sale',
            field=models.ForeignKey(to='sale.Sale_S'),
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.AddField(
            model_name='sale_s',
            name='product',
            field=models.ManyToManyField(to='product.Product', through='sale.Sales_Detail'),
        ),
    ]
