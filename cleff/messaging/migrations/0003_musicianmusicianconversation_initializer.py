# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150801_1847'),
        ('messaging', '0002_auto_20150801_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicianmusicianconversation',
            name='initializer',
            field=models.ForeignKey(related_name='initializer', default='', blank=True, to='profiles.Musician'),
            preserve_default=False,
        ),
    ]
