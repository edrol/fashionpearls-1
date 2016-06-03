# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='sale_detail',
            name='product',
        ),
        migrations.RemoveField(
            model_name='sale_detail',
            name='sale',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.DeleteModel(
            name='Sale_Detail',
        ),
    ]
