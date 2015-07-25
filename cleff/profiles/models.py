from django.contrib.auth.models import User
from django.db import models

# Create your models here.


GENRES = (
    ('Alternative', 'Alternative'),
    ('Anime', 'Anime'),
    ('Blues', 'Blues'),
    ('Childrens Music', 'Childrens Music'),
    ('Classical', 'Classical'),
    ('Comedy', 'Comedy'),
    ('Commercial', 'Commercial'),
    ('Country', 'Country'),
    ('Dance', 'Dance'),
    ('Electronic', 'Electronic'),
    ('Pop', 'Pop'),
    ('Indie', 'Indie'),
    ('Bluegrass', 'Bluegrass'),
    ('Gospel', 'Gospel'),
    ('Hip-Hop', 'Hip-Hop'),
    ('Rap', 'Rap'),
    ('Instrumental', 'Instrumental'),
    ('Jazz', 'Jazz'),
    ('Latin', 'Latin'),
    ('New Age', 'New Age'),
    ('R&B/Soul', 'R&B/Soul'),
    ('Reggae', 'Reggae'),
    ('Rock', 'Rock'),
    ('Singer', 'Singer'),
    ('Songwriter', 'Songwriter'),
    ('Vocal', 'Vocal'),
    ('World', 'World'),
    ('Metal', 'Metal'),

)

DAYS = (
    ('Mon', 'Monday'),
    ('Tues', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thurs', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),

)

TIMES = (
    ('01:00', '1 am (01:00)'), ('01:00', '1 am (01:00)'),
    ('02:00', '2 am (02:00)'), ('02:00', '2 am (02:00)'),
    ('03:00', '3 am (03:00)'), ('03:00', '3 am (03:00)'),
    ('04:00', '4 am (04:00)'), ('04:00', '4 am (04:00)'),
    ('05:00', '5 am (05:00)'), ('05:00', '5 am (05:00)'),
    ('06:00', '6 am (06:00)'), ('06:00', '6 am (06:00)'),
    ('07:00', '7 am (07:00)'), ('07:00', '7 am (07:00)'),
    ('08:00', '8 am (08:00)'), ('08:00', '8 am (08:00)'),
    ('09:00', '9 am (09:00)'), ('09:00', '9 am (09:00)'),
    ('10:00', '10 am (10:00)'), ('10:00', '10 am (10:00)'),
    ('11:00', '11 am (11:00)'), ('11:00', '11 am (11:00)'),
    ('12:00', '12 pm (12:00)'), ('12:00', '12 pm (12:00)'),
    ('13:00', '1 pm (13:00)'), ('13:00', '1 pm (13:00)'),
    ('14:00', '2 pm (14:00)'), ('14:00', '2 pm (14:00)'),
    ('15:00', '3 pm (15:00)'), ('15:00', '3 pm (15:00)'),
    ('16:00', '4 pm (16:00)'), ('16:00', '4 pm (16:00)'),
    ('17:00', '5 pm (17:00)'), ('17:00', '5 pm (17:00)'),
    ('18:00', '6 pm (18:00)'), ('18:00', '6 pm (18:00)'),
    ('19:00', '7 pm (19:00)'), ('19:00', '7 pm (19:00)'),
    ('20:00', '8 pm (20:00)'), ('20:00', '8 pm (20:00)'),
    ('21:00', '9 pm (21:00'), ('21:00', '9 pm (21:00'),
    ('22:00', '10 pm (22:00)'), ('22:00', '10 pm (22:00)'),
    ('23:00', '11 pm (23:00)'), ('23:00', '11 pm (23:00)'),
    ('24:00', '12 am (24:00)'), ('24:00', '12 am (24:00)'),

)
class ProfileModel(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d')

    class Meta:
        abstract = True


class Musician(ProfileModel):
    genres = models.ManyToManyField(through='Genre')
    summary = models.TextField(blank=True)
    company = models.CharField(max_length=60, blank=True)
    video = models.ManyToManyField('Video', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    availability = models.ManyToManyField('TimeFrame')


class NonMusician(ProfileModel):
    summary = models.TextField(blank=True)
    company = models.CharField(max_length=60, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Genre(models.Model):
    genre = models.CharField(choices=GENRES)
    description = models.CharField(max_length=140, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Video(models.Model):
    title = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    embedded_code = models.CharField(max_length=20, blank=True)
    upload = models.FileField(upload_to='', blank=True)

class TimeFrame(models.Model):
    day = models.CharField(choices=DAYS)
    start = models.CharField(choices=TIMES)
    end = models.CharField(choices=TIMES)
    timestamp = models.DateTimeField(auto_now_add=True)




