# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_location_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='location',
            new_name='current_location',
        ),
        migrations.RenameField(
            model_name='nonmusician',
            old_name='location',
            new_name='current_location',
        ),
    ]
