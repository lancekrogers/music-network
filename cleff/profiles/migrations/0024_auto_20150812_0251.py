# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0023_auto_20150812_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedmusician',
            name='date_stamp',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2015, 8, 12, 2, 51, 34, 131184, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='savedmusician',
            name='saver_musician',
            field=models.ForeignKey(blank=True, null=True, to='profiles.Musician'),
        ),
    ]
