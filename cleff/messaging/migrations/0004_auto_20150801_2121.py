# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_musicianmusicianconversation_initializer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musicianmusicianconversation',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='musicianmusicianconversation',
            name='messages',
            field=models.ManyToManyField(blank=True, to='messaging.MusMusMessage'),
        ),
        migrations.AlterField(
            model_name='musicianmusicianconversation',
            name='initializer',
            field=models.ForeignKey(to='profiles.Musician', related_name='initializer'),
        ),
        migrations.AlterField(
            model_name='musmusmessage',
            name='sender',
            field=models.ForeignKey(to='profiles.Musician', related_name='sender'),
        ),
    ]
