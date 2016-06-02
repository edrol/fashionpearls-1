# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=15, verbose_name=b'code')),
                ('name', models.CharField(max_length=50, verbose_name=b'product name')),
                ('cost', models.DecimalField(default=0.0, verbose_name=b'cost price', max_digits=5, decimal_places=2)),
                ('sale', models.DecimalField(default=0.0, verbose_name=b'sale price', max_digits=5, decimal_places=2)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('active', models.CharField(default=b'1', max_length=1, verbose_name=b'active', choices=[(b'1', b'active'), (b'0', b'inactive')])),
                ('category', models.ForeignKey(blank=True, to='product.Category', null=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
    ]
