# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150728_2142'),
    ]

    operations = [
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
            model_name='timeframe',
            name='user_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='video',
            name='genre',
            field=models.ManyToManyField(to='profiles.Genre'),
        ),
        migrations.AddField(
            model_name='video',
            name='user_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.CharField(verbose_name='Genre Description', max_length=140, blank=True),
        ),
        migrations.AlterField(
            model_name='instrumentgroup',
            name='description',
            field=models.CharField(verbose_name='Briefly describe your instrument', max_length=50),
        ),
        migrations.AlterField(
            model_name='instrumentgroup',
            name='family',
            field=models.CharField(choices=[('Percussion', 'Percussion'), ('Strings', 'Strings'), ('KPO', 'Keyboard, Piano, or Organ'), ('Woodwind', 'Woodwind'), ('Brass', 'Brass'), ('Electronic', 'Electronic'), ('CG', 'Computer Generated'), ('Vocal', 'Vocal'), ('UCMI', 'Unconventional Musical Instrument'), ('Other', 'Other')], verbose_name='Select The Instrument Family that best fits you', max_length=60),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(verbose_name='If you would like to describe your location do it here', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='musician',
            name='summary',
            field=models.TextField(verbose_name='Your Bio Goes Here', blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='embedded_code',
            field=models.CharField(verbose_name='Paste Youtube video Url here\nor upload a video below', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(verbose_name='Video Title', max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload',
            field=models.FileField(upload_to='video/%Y/%m/%d/title', verbose_name='Upload Video', blank=True),
        ),
    ]
