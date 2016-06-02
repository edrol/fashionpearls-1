# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
        ('product', '0002_auto_20160525_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'date')),
            ],
            options={
                'verbose_name': 'buy',
                'verbose_name_plural': 'shopping',
            },
        ),
        migrations.CreateModel(
            name='Purchase_Detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(max_length=9)),
                ('buy', models.ForeignKey(to='shopping.Buy')),
                ('product', models.ForeignKey(to='product.Product')),
            ],
            options={
                'verbose_name': 'purchase detail',
                'verbose_name_plural': 'details shopping',
            },
        ),
        migrations.AddField(
            model_name='buy',
            name='product',
            field=models.ManyToManyField(to='product.Product', through='shopping.Purchase_Detail'),
        ),
        migrations.AddField(
            model_name='buy',
            name='provider',
            field=models.ForeignKey(to='provider.Provider'),
        ),
    ]
