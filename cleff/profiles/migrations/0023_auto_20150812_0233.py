# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_auto_20150810_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedmusician',
            name='date_stamp',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='savedmusician',
            name='saver_nonmusician',
            field=models.ForeignKey(to='profiles.NonMusician', null=True, blank=True),
        ),
    ]
