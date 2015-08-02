# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150801_1847'),
        ('Forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musicianpost',
            options={'ordering': ['-score', '-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='musicianresponse',
            options={'ordering': ['-score', '-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='nonmusicianpost',
            options={'ordering': ['-score', '-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='nonmusicianresponse',
            options={'ordering': ['-score', '-timestamp']},
        ),
        migrations.AddField(
            model_name='musicianpost',
            name='location',
            field=models.ForeignKey(to='profiles.Location', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nonmusicianpost',
            name='location',
            field=models.ForeignKey(to='profiles.Location', default=''),
            preserve_default=False,
        ),
    ]
