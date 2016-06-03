# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_auto_20160602_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale_s',
            old_name='custom',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='sale_s',
            old_name='employ',
            new_name='employee',
        ),
    ]
