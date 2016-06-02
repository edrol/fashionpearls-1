# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.DecimalField(max_digits=10, decimal_places=2)),
                ('precio', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comision', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
