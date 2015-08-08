# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20150808_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comrade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('musicians', models.ManyToManyField(blank=True, to='profiles.SavedMusician')),
            ],
        ),
        migrations.AddField(
            model_name='musician',
            name='comrades',
            field=models.ManyToManyField(blank=True, to='profiles.Comrade'),
        ),
        migrations.AddField(
            model_name='nonmusician',
            name='comrades',
            field=models.ManyToManyField(blank=True, to='profiles.Comrade'),
        ),
    ]
