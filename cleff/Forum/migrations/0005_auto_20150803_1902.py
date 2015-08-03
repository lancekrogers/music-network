# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20150801_1847'),
        ('Forum', '0004_auto_20150803_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianResponseNonMusicianPost',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='Forum.NonMusicianPost')),
                ('user', models.ForeignKey(to='profiles.Musician')),
                ('votes', models.ManyToManyField(to='Forum.Vote', blank=True)),
            ],
            options={
                'ordering': ['-score', '-timestamp'],
            },
        ),
        migrations.AlterField(
            model_name='musicianresponse',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote', blank=True),
        ),
        migrations.AlterField(
            model_name='nonmusicianresponse',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote', blank=True),
        ),
    ]
