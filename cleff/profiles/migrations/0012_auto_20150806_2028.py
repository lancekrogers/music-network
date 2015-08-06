# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20150804_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
