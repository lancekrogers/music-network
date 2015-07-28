# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('genre', models.CharField(choices=[('Alternative', 'Alternative'), ('Anime', 'Anime'), ('Blues', 'Blues'), ('Childrens Music', 'Childrens Music'), ('Classical', 'Classical'), ('Comedy', 'Comedy'), ('Commercial', 'Commercial'), ('Country', 'Country'), ('Dance', 'Dance'), ('Electronic', 'Electronic'), ('Pop', 'Pop'), ('Indie', 'Indie'), ('Bluegrass', 'Bluegrass'), ('Gospel', 'Gospel'), ('Hip-Hop', 'Hip-Hop'), ('Rap', 'Rap'), ('Instrumental', 'Instrumental'), ('Jazz', 'Jazz'), ('Latin', 'Latin'), ('New Age', 'New Age'), ('R&B/Soul', 'R&B/Soul'), ('Reggae', 'Reggae'), ('Rock', 'Rock'), ('Singer', 'Singer'), ('Songwriter', 'Songwriter'), ('Vocal', 'Vocal'), ('World', 'World'), ('Metal', 'Metal')], max_length=20)),
                ('description', models.CharField(max_length=140, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentGroup',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('family', models.CharField(choices=[('Percussion', 'Percussion'), ('Strings', 'Strings'), ('KPO', 'Keyboard, Piano, or Organ'), ('Woodwind', 'Woodwind'), ('Brass', 'Brass'), ('Electronic', 'Electronic'), ('CG', 'Computer Generated'), ('Vocal', 'Vocal'), ('UCMI', 'Unconventional Musical Instrument'), ('Other', 'Other')], max_length=60)),
                ('description', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('zipcode', models.CharField(max_length=12, blank=True)),
                ('city', models.CharField(max_length=20, blank=True)),
                ('description', models.CharField(max_length=20, blank=True)),
                ('latitude', models.DecimalField(max_digits=200, decimal_places=10, blank=True)),
                ('longitude', models.DecimalField(max_digits=200, decimal_places=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=200, decimal_places=10, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=200, decimal_places=10, blank=True)),
                ('first_name', models.CharField(max_length=15, blank=True)),
                ('last_name', models.CharField(max_length=15, blank=True)),
                ('profile_image', models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)),
                ('summary', models.TextField(blank=True)),
                ('company', models.CharField(max_length=60, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonMusician',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=200, decimal_places=10, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=200, decimal_places=10, blank=True)),
                ('first_name', models.CharField(max_length=15, blank=True)),
                ('last_name', models.CharField(max_length=15, blank=True)),
                ('profile_image', models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)),
                ('summary', models.TextField(blank=True)),
                ('company', models.CharField(max_length=60, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locations', models.ManyToManyField(to='profiles.Location', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeFrame',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('day', models.CharField(choices=[('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thurs', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=10)),
                ('start', models.CharField(choices=[('01:00', '1 am'), ('01:30', '1:30 am'), ('02:00', '2 am'), ('02:30', '2:30 am'), ('03:00', '3 am'), ('03:30', '3:30 am'), ('04:00', '4 am'), ('04:30', '4:30 am'), ('05:00', '5 am'), ('05:30', '5:30 am'), ('06:00', '6 am'), ('06:30', '6:30 am'), ('07:00', '7 am'), ('07:30', '7:30 am'), ('08:00', '8 am'), ('08:30', '8:30 am'), ('09:00', '9 am'), ('09:30', '9:30 am'), ('10:00', '10 am'), ('10:30', '10:30 am'), ('11:00', '11 am'), ('11:30', '11:30 am'), ('12:00', '12 pm'), ('12:30', '12:30 pm'), ('13:00', '1 pm'), ('13:30', '1:30 pm'), ('14:00', '2 pm'), ('14:30', '2:30 pm'), ('15:00', '3 pm'), ('15:30', '3:30 pm'), ('16:00', '4 pm'), ('16:30', '4:30 pm'), ('17:00', '5 pm'), ('17:30', '5:30 pm'), ('18:00', '6 pm'), ('18:30', '6:30 pm'), ('19:00', '7 pm'), ('19:30', '7:30 pm'), ('20:00', '8 pm'), ('20:30', '8:30 pm'), ('21:00', '9 pm'), ('21:30', '9:30 pm'), ('22:00', '10 pm'), ('22:30', '10:30 pm'), ('23:00', '11 pm'), ('23:30', '11:30 pm'), ('24:00', '12 am'), ('24:30', '12:30 am')], max_length=10)),
                ('end', models.CharField(choices=[('01:00', '1 am'), ('01:30', '1:30 am'), ('02:00', '2 am'), ('02:30', '2:30 am'), ('03:00', '3 am'), ('03:30', '3:30 am'), ('04:00', '4 am'), ('04:30', '4:30 am'), ('05:00', '5 am'), ('05:30', '5:30 am'), ('06:00', '6 am'), ('06:30', '6:30 am'), ('07:00', '7 am'), ('07:30', '7:30 am'), ('08:00', '8 am'), ('08:30', '8:30 am'), ('09:00', '9 am'), ('09:30', '9:30 am'), ('10:00', '10 am'), ('10:30', '10:30 am'), ('11:00', '11 am'), ('11:30', '11:30 am'), ('12:00', '12 pm'), ('12:30', '12:30 pm'), ('13:00', '1 pm'), ('13:30', '1:30 pm'), ('14:00', '2 pm'), ('14:30', '2:30 pm'), ('15:00', '3 pm'), ('15:30', '3:30 pm'), ('16:00', '4 pm'), ('16:30', '4:30 pm'), ('17:00', '5 pm'), ('17:30', '5:30 pm'), ('18:00', '6 pm'), ('18:30', '6:30 pm'), ('19:00', '7 pm'), ('19:30', '7:30 pm'), ('20:00', '8 pm'), ('20:30', '8:30 pm'), ('21:00', '9 pm'), ('21:30', '9:30 pm'), ('22:00', '10 pm'), ('22:30', '10:30 pm'), ('23:00', '11 pm'), ('23:30', '11:30 pm'), ('24:00', '12 am'), ('24:30', '12:30 am')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('embedded_code', models.CharField(max_length=20, blank=True)),
                ('upload', models.FileField(upload_to='video/%Y/%m/%d', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='musician',
            name='availability',
            field=models.ManyToManyField(to='profiles.TimeFrame', blank=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='genres',
            field=models.ManyToManyField(to='profiles.Genre', blank=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='instrument_group',
            field=models.ManyToManyField(to='profiles.InstrumentGroup'),
        ),
        migrations.AddField(
            model_name='musician',
            name='locations',
            field=models.ManyToManyField(to='profiles.Location', blank=True),
        ),
        migrations.AddField(
            model_name='musician',
            name='video',
            field=models.ManyToManyField(to='profiles.Video', blank=True),
        ),
    ]
