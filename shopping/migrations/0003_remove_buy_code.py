# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20160526_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='code',
        ),
    ]
