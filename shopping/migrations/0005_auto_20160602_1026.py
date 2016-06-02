# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_buy_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='code',
            new_name='invoice',
        ),
    ]
