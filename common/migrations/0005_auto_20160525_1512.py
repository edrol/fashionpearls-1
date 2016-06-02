# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20160525_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(default=b'-', max_length=1, verbose_name=b'gender', choices=[(b'-', b'Others'), (b'F', b'Female'), (b'M', b'Male')]),
        ),
    ]
