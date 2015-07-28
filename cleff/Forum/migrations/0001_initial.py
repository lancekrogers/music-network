# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicianPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('text', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-score', 'timestamp'],
            },
        ),
        migrations.CreateModel(
            name='MusicianResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='Forum.MusicianPost')),
                ('user', models.ForeignKey(to='profiles.Musician')),
            ],
            options={
                'ordering': ['-score', 'timestamp'],
            },
        ),
        migrations.CreateModel(
            name='NonMusicianPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('text', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-score', 'timestamp'],
            },
        ),
        migrations.CreateModel(
            name='NonMusicianResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('score', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='Forum.NonMusicianPost')),
                ('user', models.ForeignKey(to='profiles.NonMusician')),
            ],
            options={
                'ordering': ['-score', 'timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=45)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votee_pk', models.IntegerField(default=-1)),
                ('upvote', models.BooleanField(default=False)),
                ('downvote', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_post', models.BooleanField(default=False)),
                ('is_response', models.BooleanField(default=False)),
                ('voter', models.ForeignKey(to='profiles.Musician', default=None)),
            ],
        ),
        migrations.AddField(
            model_name='nonmusicianresponse',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote'),
        ),
        migrations.AddField(
            model_name='nonmusicianpost',
            name='tags',
            field=models.ManyToManyField(to='Forum.Tag'),
        ),
        migrations.AddField(
            model_name='nonmusicianpost',
            name='user',
            field=models.ForeignKey(to='profiles.NonMusician'),
        ),
        migrations.AddField(
            model_name='nonmusicianpost',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote'),
        ),
        migrations.AddField(
            model_name='musicianresponse',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote'),
        ),
        migrations.AddField(
            model_name='musicianpost',
            name='tags',
            field=models.ManyToManyField(to='Forum.Tag'),
        ),
        migrations.AddField(
            model_name='musicianpost',
            name='user',
            field=models.ForeignKey(to='profiles.Musician'),
        ),
        migrations.AddField(
            model_name='musicianpost',
            name='votes',
            field=models.ManyToManyField(to='Forum.Vote'),
        ),
    ]
