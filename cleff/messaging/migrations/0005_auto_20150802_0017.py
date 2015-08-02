# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0004_auto_20150801_2121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='musmusmessage',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RemoveField(
            model_name='musmusmessage',
            name='conversation',
        ),
        migrations.AddField(
            model_name='musmusmessage',
            name='conversation',
            field=models.ManyToManyField(to='messaging.MusicianMusicianConversation'),
        ),
    ]
