# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0009_auto_20150804_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musicianpost',
            options={'ordering': ['-timestamp', '-score']},
        ),
        migrations.AlterModelOptions(
            name='musicianresponse',
            options={'ordering': ['-timestamp', '-score']},
        ),
        migrations.AlterField(
            model_name='nonmusicianpost',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
