# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0008_auto_20150804_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonmusicianresponse',
            name='musician',
            field=models.ForeignKey(blank=True, null=True, to='profiles.Musician'),
        ),
        migrations.AlterField(
            model_name='nonmusicianresponse',
            name='nonmusician',
            field=models.ForeignKey(blank=True, null=True, to='profiles.NonMusician'),
        ),
    ]
