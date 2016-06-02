# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10, null=True, verbose_name=b'phone')),
                ('phone', models.ForeignKey(blank=True, to='common.Person', null=True)),
            ],
            options={
                'verbose_name': 'phone',
                'verbose_name_plural': 'phones',
            },
        ),
    ]
