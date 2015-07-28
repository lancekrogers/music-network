# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('genre', models.CharField(choices=[('Alternative', 'Alternative'), ('Anime', 'Anime'), ('Blues', 'Blues'), ('Childrens Music', 'Childrens Music'), ('Classical', 'Classical'), ('Comedy', 'Comedy'), ('Commercial', 'Commercial'), ('Country', 'Country'), ('Dance', 'Dance'), ('Electronic', 'Electronic'), ('Pop', 'Pop'), ('Indie', 'Indie'), ('Bluegrass', 'Bluegrass'), ('Gospel', 'Gospel'), ('Hip-Hop', 'Hip-Hop'), ('Rap', 'Rap'), ('Instrumental', 'Instrumental'), ('Jazz', 'Jazz'), ('Latin', 'Latin'), ('New Age', 'New Age'), ('R&B/Soul', 'R&B/Soul'), ('Reggae', 'Reggae'), ('Rock', 'Rock'), ('Singer', 'Singer'), ('Songwriter', 'Songwriter'), ('Vocal', 'Vocal'), ('World', 'World'), ('Metal', 'Metal')], max_length=20)),
                ('description', models.CharField(blank=True, max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('family', models.CharField(choices=[('Percussion', 'Percussion'), ('Strings', 'Strings'), ('KPO', 'Keyboard, Piano, or Organ'), ('Woodwind', 'Woodwind'), ('Brass', 'Brass'), ('Electronic', 'Electronic'), ('CG', 'Computer Generated'), ('Vocal', 'Vocal'), ('UCMI', 'Unconventional Musical Instrument'), ('Other', 'Other')], max_length=60)),
                ('description', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('zipcode', models.CharField(blank=True, max_length=12)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('description', models.CharField(blank=True, max_length=20)),
                ('latitude', models.DecimalField(decimal_places=10, blank=True, max_digits=200)),
                ('longitude', models.DecimalField(decimal_places=10, blank=True, max_digits=200)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('latitude', models.DecimalField(decimal_places=10, blank=True, null=True, max_digits=200)),
                ('longitude', models.DecimalField(decimal_places=10, blank=True, null=True, max_digits=200)),
                ('first_name', models.CharField(blank=True, max_length=15)),
                ('last_name', models.CharField(blank=True, max_length=15)),
                ('profile_image', models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)),
                ('summary', models.TextField(blank=True)),
                ('company', models.CharField(blank=True, max_length=60)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonMusician',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('latitude', models.DecimalField(decimal_places=10, blank=True, null=True, max_digits=200)),
                ('longitude', models.DecimalField(decimal_places=10, blank=True, null=True, max_digits=200)),
                ('first_name', models.CharField(blank=True, max_length=15)),
                ('last_name', models.CharField(blank=True, max_length=15)),
                ('profile_image', models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)),
                ('summary', models.TextField(blank=True)),
                ('company', models.CharField(blank=True, max_length=60)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locations', models.ManyToManyField(blank=True, to='profiles.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimeFrame',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('day', models.CharField(choices=[('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thurs', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=10)),
                ('start', models.CharField(choices=[('01:00', '1 am'), ('01:30', '1:30 am'), ('02:00', '2 am'), ('02:30', '2:30 am'), ('03:00', '3 am'), ('03:30', '3:30 am'), ('04:00', '4 am'), ('04:30', '4:30 am'), ('05:00', '5 am'), ('05:30', '5:30 am'), ('06:00', '6 am'), ('06:30', '6:30 am'), ('07:00', '7 am'), ('07:30', '7:30 am'), ('08:00', '8 am'), ('08:30', '8:30 am'), ('09:00', '9 am'), ('09:30', '9:30 am'), ('10:00', '10 am'), ('10:30', '10:30 am'), ('11:00', '11 am'), ('11:30', '11:30 am'), ('12:00', '12 pm'), ('12:30', '12:30 pm'), ('13:00', '1 pm'), ('13:30', '1:30 pm'), ('14:00', '2 pm'), ('14:30', '2:30 pm'), ('15:00', '3 pm'), ('15:30', '3:30 pm'), ('16:00', '4 pm'), ('16:30', '4:30 pm'), ('17:00', '5 pm'), ('17:30', '5:30 pm'), ('18:00', '6 pm'), ('18:30', '6:30 pm'), ('19:00', '7 pm'), ('19:30', '7:30 pm'), ('20:00', '8 pm'), ('20:30', '8:30 pm'), ('21:00', '9 pm'), ('21:30', '9:30 pm'), ('22:00', '10 pm'), ('22:30', '10:30 pm'), ('23:00', '11 pm'), ('23:30', '11:30 pm'), ('24:00', '12 am'), ('24:30', '12:30 am')], max_length=10)),
                ('end', models.CharField(choices=[('01:00', '1 am'), ('01:30', '1:30 am'), ('02:00', '2 am'), ('02:30', '2:30 am'), ('03:00', '3 am'), ('03:30', '3:30 am'), ('04:00', '4 am'), ('04:30', '4:30 am'), ('05:00', '5 am'), ('05:30', '5:30 am'), ('06:00', '6 am'), ('06:30', '6:30 am'), ('07:00', '7 am'), ('07:30', '7:30 am'), ('08:00', '8 am'), ('08:30', '8:30 am'), ('09:00', '9 am'), ('09:30', '9:30 am'), ('10:00', '10 am'), ('10:30', '10:30 am'), ('11:00', '11 am'), ('11:30', '11:30 am'), ('12:00', '12 pm'), ('12:30', '12:30 pm'), ('13:00', '1 pm'), ('13:30', '1:30 pm'), ('14:00', '2 pm'), ('14:30', '2:30 pm'), ('15:00', '3 pm'), ('15:30', '3:30 pm'), ('16:00', '4 pm'), ('16:30', '4:30 pm'), ('17:00', '5 pm'), ('17:30', '5:30 pm'), ('18:00', '6 pm'), ('18:30', '6:30 pm'), ('19:00', '7 pm'), ('19:30', '7:30 pm'), ('20:00', '8 pm'), ('20:30', '8:30 pm'), ('21:00', '9 pm'), ('21:30', '9:30 pm'), ('22:00', '10 pm'), ('22:30', '10:30 pm'), ('23:00', '11 pm'), ('23:30', '11:30 pm'), ('24:00', '12 am'), ('24:30', '12:30 am')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to='profiles.Musician', related_name='users_availability')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('embedded_code', models.CharField(blank=True, max_length=20)),
                ('upload', models.FileField(upload_to='video/%Y/%m/%d/title', blank=True)),
                ('uploader', models.ForeignKey(to='profiles.Musician', related_name='uploaded_videos')),
            ],
        ),
        migrations.AddField(
            model_name='musician',
            name='availability',
            field=models.ManyToManyField(blank=True, to='profiles.TimeFrame'),
        ),
        migrations.AddField(
            model_name='musician',
            name='genres',
            field=models.ManyToManyField(blank=True, to='profiles.Genre'),
        ),
        migrations.AddField(
            model_name='musician',
            name='instrument_group',
            field=models.ManyToManyField(to='profiles.InstrumentGroup'),
        ),
        migrations.AddField(
            model_name='musician',
            name='locations',
            field=models.ManyToManyField(blank=True, to='profiles.Location'),
        ),
        migrations.AddField(
            model_name='musician',
            name='video',
            field=models.ManyToManyField(blank=True, to='profiles.Video'),
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_location'),
        ),
        migrations.AddField(
            model_name='instrumentgroup',
            name='user',
            field=models.ForeignKey(to='profiles.Musician', related_name='instruments'),
        ),
    ]
