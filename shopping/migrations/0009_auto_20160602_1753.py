# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_auto_20160602_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_detail',
            name='product',
            field=models.ForeignKey(to='product.Product', null=True),
        ),
    ]
