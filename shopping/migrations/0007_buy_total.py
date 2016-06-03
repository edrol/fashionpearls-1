# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_auto_20160602_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='total',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
