# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20160525_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Person')),
                ('address', models.CharField(max_length=40, null=True, verbose_name=b'fiscal address')),
            ],
            options={
                'verbose_name': 'provider',
                'verbose_name_plural': 'providers',
            },
            bases=('common.person',),
        ),
    ]
