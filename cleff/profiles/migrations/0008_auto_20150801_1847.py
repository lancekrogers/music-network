# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20150731_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentgroup',
            name='family',
            field=models.CharField(choices=[('Percussion', 'Percussion'), ('Guitar', 'Guitar'), ('Bass', 'Bass'), ('Banjo', 'Banjo'), ('Upright Bass', 'Upright Bass'), ('Violin', 'Violin'), ('Chello', 'Chello'), ('Strings', 'Strings'), ('Lute', 'Lute'), ('KPO', 'Keyboard, Piano, or Organ'), ('Woodwind', 'Woodwind'), ('Brass', 'Brass'), ('Electronic', 'Electronic'), ('CG', 'Computer Generated'), ('Vocal', 'Vocal'), ('UCMI', 'Unconventional Musical Instrument'), ('Other', 'Other')], max_length=60),
        ),
        migrations.AlterField(
            model_name='timeframe',
            name='end',
            field=models.CharField(choices=[('1 am', '1 am'), ('1:30 am', '1:30 am'), ('2 am', '2 am'), ('2:30 am', '2:30 am'), ('3 am', '3 am'), ('3:30 am', '3:30 am'), ('4 am', '4 am'), ('4:30 am', '4:30 am'), ('5 am', '5 am'), ('5:30 am', '5:30 am'), ('6 am', '6 am'), ('6:30 am', '6:30 am'), ('7 am', '7 am'), ('7:30 am', '7:30 am'), ('8 am', '8 am'), ('8:30 am', '8:30 am'), ('9 am', '9 am'), ('9:30 am', '9:30 am'), ('10 am', '10 am'), ('10:30 am', '10:30 am'), ('11 am', '11 am'), ('11:30 am', '11:30 am'), ('12 pm', '12 pm'), ('12:30 pm', '12:30 pm'), ('1 pm', '1 pm'), ('1:30 pm', '1:30 pm'), ('2 pm', '2 pm'), ('2:30 pm', '2:30 pm'), ('3 pm', '3 pm'), ('3:30 pm', '3:30 pm'), ('4 pm', '4 pm'), ('4:30 pm', '4:30 pm'), ('5 pm', '5 pm'), ('5:30 pm', '5:30 pm'), ('6 pm', '6 pm'), ('6:30 pm', '6:30 pm'), ('7 pm', '7 pm'), ('7:30 pm', '7:30 pm'), ('8 pm', '8 pm'), ('8:30 pm', '8:30 pm'), ('9 pm', '9 pm'), ('9:30 pm', '9:30 pm'), ('10 pm', '10 pm'), ('10:30 pm', '10:30 pm'), ('11 pm', '11 pm'), ('11:30 pm', '11:30 pm'), ('12 pm', '12 am'), ('12:30 am', '12:30 am')], max_length=10),
        ),
        migrations.AlterField(
            model_name='timeframe',
            name='start',
            field=models.CharField(choices=[('1 am', '1 am'), ('1:30 am', '1:30 am'), ('2 am', '2 am'), ('2:30 am', '2:30 am'), ('3 am', '3 am'), ('3:30 am', '3:30 am'), ('4 am', '4 am'), ('4:30 am', '4:30 am'), ('5 am', '5 am'), ('5:30 am', '5:30 am'), ('6 am', '6 am'), ('6:30 am', '6:30 am'), ('7 am', '7 am'), ('7:30 am', '7:30 am'), ('8 am', '8 am'), ('8:30 am', '8:30 am'), ('9 am', '9 am'), ('9:30 am', '9:30 am'), ('10 am', '10 am'), ('10:30 am', '10:30 am'), ('11 am', '11 am'), ('11:30 am', '11:30 am'), ('12 pm', '12 pm'), ('12:30 pm', '12:30 pm'), ('1 pm', '1 pm'), ('1:30 pm', '1:30 pm'), ('2 pm', '2 pm'), ('2:30 pm', '2:30 pm'), ('3 pm', '3 pm'), ('3:30 pm', '3:30 pm'), ('4 pm', '4 pm'), ('4:30 pm', '4:30 pm'), ('5 pm', '5 pm'), ('5:30 pm', '5:30 pm'), ('6 pm', '6 pm'), ('6:30 pm', '6:30 pm'), ('7 pm', '7 pm'), ('7:30 pm', '7:30 pm'), ('8 pm', '8 pm'), ('8:30 pm', '8:30 pm'), ('9 pm', '9 pm'), ('9:30 pm', '9:30 pm'), ('10 pm', '10 pm'), ('10:30 pm', '10:30 pm'), ('11 pm', '11 pm'), ('11:30 pm', '11:30 pm'), ('12 pm', '12 am'), ('12:30 am', '12:30 am')], max_length=10),
        ),
    ]
