# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_email'),
        ('product', '0002_auto_20160525_1958'),
        ('employee', '0001_initial'),
        ('sale', '0002_auto_20160602_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
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
        migrations.CreateModel(
            name='Sales_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(to='product.Product', null=True)),
                ('sale', models.ForeignKey(to='sale.Sale')),
            ],
            options={
                'verbose_name': 'details sale',
                'verbose_name_plural': 'details sales',
            },
        ),
    ]
