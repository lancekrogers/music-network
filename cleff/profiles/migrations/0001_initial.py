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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('genre', models.CharField(max_length=20, choices=[('Alternative', 'Alternative'), ('Anime', 'Anime'), ('Blues', 'Blues'), ('Childrens Music', 'Childrens Music'), ('Classical', 'Classical'), ('Comedy', 'Comedy'), ('Commercial', 'Commercial'), ('Country', 'Country'), ('Dance', 'Dance'), ('Electronic', 'Electronic'), ('Pop', 'Pop'), ('Indie', 'Indie'), ('Bluegrass', 'Bluegrass'), ('Gospel', 'Gospel'), ('Hip-Hop', 'Hip-Hop'), ('Rap', 'Rap'), ('Instrumental', 'Instrumental'), ('Jazz', 'Jazz'), ('Latin', 'Latin'), ('New Age', 'New Age'), ('R&B/Soul', 'R&B/Soul'), ('Reggae', 'Reggae'), ('Rock', 'Rock'), ('Singer', 'Singer'), ('Songwriter', 'Songwriter'), ('Vocal', 'Vocal'), ('World', 'World'), ('Metal', 'Metal')])),
                ('description', models.CharField(blank=True, max_length=140)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
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
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
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
            name='TimeFrame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('day', models.CharField(max_length=10, choices=[('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thurs', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')])),
                ('start', models.CharField(max_length=20, choices=[('01:00', '1 am (01:00)'), ('01:00', '1 am (01:00)'), ('02:00', '2 am (02:00)'), ('02:00', '2 am (02:00)'), ('03:00', '3 am (03:00)'), ('03:00', '3 am (03:00)'), ('04:00', '4 am (04:00)'), ('04:00', '4 am (04:00)'), ('05:00', '5 am (05:00)'), ('05:00', '5 am (05:00)'), ('06:00', '6 am (06:00)'), ('06:00', '6 am (06:00)'), ('07:00', '7 am (07:00)'), ('07:00', '7 am (07:00)'), ('08:00', '8 am (08:00)'), ('08:00', '8 am (08:00)'), ('09:00', '9 am (09:00)'), ('09:00', '9 am (09:00)'), ('10:00', '10 am (10:00)'), ('10:00', '10 am (10:00)'), ('11:00', '11 am (11:00)'), ('11:00', '11 am (11:00)'), ('12:00', '12 pm (12:00)'), ('12:00', '12 pm (12:00)'), ('13:00', '1 pm (13:00)'), ('13:00', '1 pm (13:00)'), ('14:00', '2 pm (14:00)'), ('14:00', '2 pm (14:00)'), ('15:00', '3 pm (15:00)'), ('15:00', '3 pm (15:00)'), ('16:00', '4 pm (16:00)'), ('16:00', '4 pm (16:00)'), ('17:00', '5 pm (17:00)'), ('17:00', '5 pm (17:00)'), ('18:00', '6 pm (18:00)'), ('18:00', '6 pm (18:00)'), ('19:00', '7 pm (19:00)'), ('19:00', '7 pm (19:00)'), ('20:00', '8 pm (20:00)'), ('20:00', '8 pm (20:00)'), ('21:00', '9 pm (21:00'), ('21:00', '9 pm (21:00'), ('22:00', '10 pm (22:00)'), ('22:00', '10 pm (22:00)'), ('23:00', '11 pm (23:00)'), ('23:00', '11 pm (23:00)'), ('24:00', '12 am (24:00)'), ('24:00', '12 am (24:00)')])),
                ('end', models.CharField(max_length=20, choices=[('01:00', '1 am (01:00)'), ('01:00', '1 am (01:00)'), ('02:00', '2 am (02:00)'), ('02:00', '2 am (02:00)'), ('03:00', '3 am (03:00)'), ('03:00', '3 am (03:00)'), ('04:00', '4 am (04:00)'), ('04:00', '4 am (04:00)'), ('05:00', '5 am (05:00)'), ('05:00', '5 am (05:00)'), ('06:00', '6 am (06:00)'), ('06:00', '6 am (06:00)'), ('07:00', '7 am (07:00)'), ('07:00', '7 am (07:00)'), ('08:00', '8 am (08:00)'), ('08:00', '8 am (08:00)'), ('09:00', '9 am (09:00)'), ('09:00', '9 am (09:00)'), ('10:00', '10 am (10:00)'), ('10:00', '10 am (10:00)'), ('11:00', '11 am (11:00)'), ('11:00', '11 am (11:00)'), ('12:00', '12 pm (12:00)'), ('12:00', '12 pm (12:00)'), ('13:00', '1 pm (13:00)'), ('13:00', '1 pm (13:00)'), ('14:00', '2 pm (14:00)'), ('14:00', '2 pm (14:00)'), ('15:00', '3 pm (15:00)'), ('15:00', '3 pm (15:00)'), ('16:00', '4 pm (16:00)'), ('16:00', '4 pm (16:00)'), ('17:00', '5 pm (17:00)'), ('17:00', '5 pm (17:00)'), ('18:00', '6 pm (18:00)'), ('18:00', '6 pm (18:00)'), ('19:00', '7 pm (19:00)'), ('19:00', '7 pm (19:00)'), ('20:00', '8 pm (20:00)'), ('20:00', '8 pm (20:00)'), ('21:00', '9 pm (21:00'), ('21:00', '9 pm (21:00'), ('22:00', '10 pm (22:00)'), ('22:00', '10 pm (22:00)'), ('23:00', '11 pm (23:00)'), ('23:00', '11 pm (23:00)'), ('24:00', '12 am (24:00)'), ('24:00', '12 am (24:00)')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('embedded_code', models.CharField(blank=True, max_length=20)),
                ('upload', models.FileField(upload_to='video/%Y/%m/%d', blank=True)),
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
            name='video',
            field=models.ManyToManyField(blank=True, to='profiles.Video'),
        ),
    ]
