# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_auto_20150809_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='comrade',
            name='date_stamp',
            field=models.DateField(default=datetime.datetime(2015, 8, 10, 3, 51, 1, 46784, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='savedmusician',
            name='date_stamp',
            field=models.DateField(default=datetime.datetime(2015, 8, 10, 3, 51, 15, 430533, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='savedmusician',
            name='saver_musician',
            field=models.ForeignKey(blank=True, default=2, to='profiles.Musician'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='savedmusician',
            name='saver_nonmusician',
            field=models.ForeignKey(blank=True, default=20, to='profiles.NonMusician'),
            preserve_default=False,
        ),
    ]
