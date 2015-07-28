# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumentgroup',
            name='user',
        ),
        migrations.RemoveField(
            model_name='location',
            name='user',
        ),
        migrations.RemoveField(
            model_name='timeframe',
            name='user',
        ),
        migrations.RemoveField(
            model_name='video',
            name='uploader',
        ),
    ]
