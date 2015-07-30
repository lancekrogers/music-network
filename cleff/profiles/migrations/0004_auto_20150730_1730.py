# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_timeframe_all_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='friends',
            field=models.ManyToManyField(blank=True, to='profiles.SavedMusician'),
        ),
        migrations.AlterField(
            model_name='musician',
            name='instrument_group',
            field=models.ManyToManyField(blank=True, to='profiles.InstrumentGroup'),
        ),
        migrations.AlterField(
            model_name='nonmusician',
            name='musicians',
            field=models.ManyToManyField(blank=True, to='profiles.SavedMusician'),
        ),
    ]
