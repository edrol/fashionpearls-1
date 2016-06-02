# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='business_name',
        ),
    ]
