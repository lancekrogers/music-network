# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150801_1847'),
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianMusicianConversation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('musician_one', models.ForeignKey(to='profiles.Musician', related_name='musician_one')),
                ('musician_two', models.ForeignKey(to='profiles.Musician', related_name='musician_two')),
            ],
        ),
        migrations.RemoveField(
            model_name='musianmusianconversation',
            name='musician_one',
        ),
        migrations.RemoveField(
            model_name='musianmusianconversation',
            name='musician_two',
        ),
        migrations.AlterField(
            model_name='musmusmessage',
            name='conversation',
            field=models.OneToOneField(to='messaging.MusicianMusicianConversation'),
        ),
        migrations.DeleteModel(
            name='MusianMusianConversation',
        ),
    ]
