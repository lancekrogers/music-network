# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20150810_0351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comrade',
            options={'ordering': ['-date_stamp']},
        ),
    ]
