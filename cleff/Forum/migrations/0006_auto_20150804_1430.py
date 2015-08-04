# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_auto_20150803_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musicianpost',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='musicianresponse',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='musicianresponsenonmusicianpost',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='nonmusicianpost',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='nonmusicianresponse',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='musicianpost',
            name='tags',
            field=models.ManyToManyField(blank=True, to='Forum.Tag'),
        ),
    ]
