# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0003_remove_buy_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='code',
            field=models.CharField(max_length=10, null=True, verbose_name=b'code'),
        ),
    ]
