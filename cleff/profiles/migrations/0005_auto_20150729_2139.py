# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150729_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedMusician',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('musicain_pk', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterField(
            model_name='nonmusician',
            name='summary',
            field=models.TextField(blank=True, verbose_name='What brings you to this site?'),
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
