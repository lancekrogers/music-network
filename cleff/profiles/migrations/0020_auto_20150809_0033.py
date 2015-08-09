# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20150808_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comrade',
            old_name='musician_pk',
            new_name='numbre',
        ),
        migrations.RenameField(
            model_name='savedmusician',
            old_name='musician_pk',
            new_name='numbre',
        ),
    ]
