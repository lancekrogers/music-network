# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedMusician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('musicain_pk', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RemoveField(
            model_name='instrumentgroup',
            name='user',
        ),
        migrations.RemoveField(
            model_name='location',
            name='user',
        ),
        migrations.RemoveField(
            model_name='timeframe',
            name='user',
        ),
        migrations.RemoveField(
            model_name='video',
            name='uploader',
        ),
        migrations.AddField(
            model_name='genre',
            name='user_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='instrumentgroup',
            name='user_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='location',
            name='user_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='musician',
            name='is_musician',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nonmusician',
            name='is_musician',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timeframe',
            name='user_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='video',
            name='genre',
            field=models.ManyToManyField(blank=True, to='profiles.Genre'),
        ),
        migrations.AddField(
            model_name='video',
            name='user_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='musician',
            name='friends',
            field=models.ManyToManyField(to='profiles.SavedMusician'),
        ),
        migrations.AddField(
            model_name='nonmusician',
            name='musicians',
            field=models.ManyToManyField(to='profiles.SavedMusician'),
        ),
    ]
