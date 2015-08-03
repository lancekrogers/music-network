# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0003_auto_20150803_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianpost',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote', blank=True),
        ),
        migrations.AlterField(
            model_name='nonmusicianpost',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote', blank=True),
        ),
    ]
