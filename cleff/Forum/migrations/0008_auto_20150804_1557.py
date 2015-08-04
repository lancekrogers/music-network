# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150801_1847'),
        ('Forum', '0007_auto_20150804_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicianresponsenonmusicianpost',
            name='post',
        ),
        migrations.RemoveField(
            model_name='musicianresponsenonmusicianpost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='musicianresponsenonmusicianpost',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='nonmusicianresponse',
            name='user',
        ),
        migrations.AddField(
            model_name='nonmusicianresponse',
            name='musician',
            field=models.ForeignKey(to='profiles.Musician', default='', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nonmusicianresponse',
            name='nonmusician',
            field=models.ForeignKey(to='profiles.NonMusician', default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='musicianpost',
            name='location',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='nonmusicianpost',
            name='location',
            field=geoposition.fields.GeopositionField(blank=True, max_length=42),
        ),
        migrations.AlterField(
            model_name='nonmusicianpost',
            name='tags',
            field=models.ManyToManyField(to='Forum.Tag', blank=True),
        ),
        migrations.DeleteModel(
            name='MusicianResponseNonMusicianPost',
        ),
    ]
