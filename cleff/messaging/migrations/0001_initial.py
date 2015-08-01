# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150801_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusianMusianConversation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('musician_one', models.ForeignKey(to='profiles.Musician', related_name='musician_one')),
                ('musician_two', models.ForeignKey(to='profiles.Musician', related_name='musician_two')),
            ],
        ),
        migrations.CreateModel(
            name='MusMusMessage',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.OneToOneField(to='messaging.MusianMusianConversation')),
                ('receiver', models.ForeignKey(to='profiles.Musician', related_name='receiver')),
                ('sender', models.OneToOneField(to='profiles.Musician', related_name='sender')),
            ],
        ),
    ]
