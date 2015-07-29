# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150729_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='is_musician',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nonmusician',
            name='is_musician',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='genre',
            field=models.ManyToManyField(blank=True, to='profiles.Genre'),
        ),
    ]
