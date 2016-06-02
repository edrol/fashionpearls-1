# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=40, verbose_name=b'address')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('nit', models.CharField(max_length=10, unique=True, serialize=False, verbose_name=b'NIT o DPI', primary_key=True)),
                ('name', models.CharField(max_length=20, null=True, verbose_name=b'name')),
                ('last_name', models.CharField(max_length=20, null=True, verbose_name=b'last name')),
                ('business_name', models.CharField(max_length=50, null=True, verbose_name=b'business name', blank=True)),
                ('gender', models.CharField(default=b'-', max_length=1, verbose_name=b'gender', choices=[(b'F', b'Female'), (b'-', b'-----'), (b'M', b'Male')])),
                ('birthday', models.DateField(null=True, verbose_name=b'birthday')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='address',
            field=models.ForeignKey(blank=True, to='common.Person', null=True),
        ),
    ]
