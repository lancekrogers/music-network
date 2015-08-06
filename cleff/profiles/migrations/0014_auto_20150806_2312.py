# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_location_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
