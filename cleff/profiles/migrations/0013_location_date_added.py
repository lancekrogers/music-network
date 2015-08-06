# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20150806_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='date_added',
            field=models.DateField(auto_now_add=True, default='1969-10-10'),
            preserve_default=False,
        ),
    ]
