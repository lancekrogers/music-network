# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_auto_20150806_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='search_range',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='nonmusician',
            name='search_range',
            field=models.IntegerField(default=50),
        ),
    ]
