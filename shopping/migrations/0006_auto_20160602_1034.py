# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20160602_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='invoice',
            field=models.CharField(max_length=10, null=True, verbose_name=b'invoice'),
        ),
    ]
