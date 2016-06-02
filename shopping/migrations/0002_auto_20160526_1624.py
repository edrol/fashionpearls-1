# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase_detail',
            options={'verbose_name': 'purchase detail', 'verbose_name_plural': 'Details shopping'},
        ),
        migrations.AddField(
            model_name='buy',
            name='code',
            field=models.CharField(max_length=10, null=True, verbose_name=b'code'),
        ),
        migrations.AlterField(
            model_name='purchase_detail',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
