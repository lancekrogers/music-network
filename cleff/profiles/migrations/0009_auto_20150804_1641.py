# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150801_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='location',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='musician',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='nonmusician',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='nonmusician',
            name='longitude',
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, blank=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, blank=True),
        ),
        migrations.AddField(
            model_name='nonmusician',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, blank=True),
        ),
    ]
