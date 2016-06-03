# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_buy_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='total',
        ),
        migrations.AddField(
            model_name='purchase_detail',
            name='cost',
            field=models.IntegerField(null=True),
        ),
    ]
