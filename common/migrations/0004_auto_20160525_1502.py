# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_person_business_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(default=b'F', max_length=1, verbose_name=b'gender', choices=[(b'-', b'Others'), (b'F', b'Female'), (b'M', b'Male')]),
        ),
    ]
