# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150731_0117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedmusician',
            old_name='musicain_pk',
            new_name='musician_pk',
        ),
    ]
