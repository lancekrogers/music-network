# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20150808_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comrade',
            name='musicians',
        ),
        migrations.AddField(
            model_name='comrade',
            name='musicians',
            field=models.ForeignKey(to='profiles.SavedMusician', blank=True, default=1),
            preserve_default=False,
        ),
    ]
