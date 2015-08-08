# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_auto_20150808_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comrade',
            name='id',
        ),
        migrations.AlterField(
            model_name='comrade',
            name='musicians',
            field=models.OneToOneField(serialize=False, to='profiles.SavedMusician', blank=True, primary_key=True),
        ),
    ]
