# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20150808_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comrade',
            old_name='musicians',
            new_name='musician_pk',
        ),
    ]
