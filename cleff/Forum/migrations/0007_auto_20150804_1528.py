# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0006_auto_20150804_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicianpost',
            name='city',
        ),
        migrations.RemoveField(
            model_name='musicianpost',
            name='states',
        ),
        migrations.RemoveField(
            model_name='nonmusicianpost',
            name='city',
        ),
        migrations.RemoveField(
            model_name='nonmusicianpost',
            name='states',
        ),
        migrations.AddField(
            model_name='musicianpost',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nonmusicianpost',
            name='location',
            field=geoposition.fields.GeopositionField(max_length=42, default=''),
            preserve_default=False,
        ),
    ]
