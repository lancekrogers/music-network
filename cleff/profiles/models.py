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
    ('01:00', '1 am'), ('01:00', '1:30 am'),
    ('02:00', '2 am'), ('02:00', '2:30 am'),
    ('03:00', '3 am'), ('03:00', '3:30 am'),
    ('04:00', '4 am'), ('04:00', '4:30 am'),
    ('05:00', '5 am)'), ('05:00', '5:30 am'),
    ('06:00', '6 am'), ('06:00', '6:30 am'),
    ('07:00', '7 am'), ('07:00', '7:30 am'),
    ('08:00', '8 am'), ('08:00', '8:30 am'),
    ('09:00', '9 am'), ('09:00', '9:30 am'),
    ('10:00', '10 am'), ('10:00', '10:30 am'),
    ('11:00', '11 am'), ('11:00', '11:30 am'),
    ('12:00', '12 pm'), ('12:00', '12:30 pm'),
    ('13:00', '1 pm'), ('13:00', '1:30 pm'),
    ('14:00', '2 pm'), ('14:00', '2:30 pm'),
    ('15:00', '3 pm'), ('15:00', '3:30 pm'),
    ('16:00', '4 pm'), ('16:00', '4:30 pm'),
    ('17:00', '5 pm'), ('17:00', '5:30 pm'),
    ('18:00', '6 pm'), ('18:00', '6:30 pm'),
    ('19:00', '7 pm'), ('19:00', '7:30 pm'),
    ('20:00', '8 pm'), ('20:00', '8:30 pm'),
    ('21:00', '9 pm'), ('21:00', '9:30 pm'),
    ('22:00', '10 pm'), ('22:00', '10:30 pm'),
    ('23:00', '11 pm'), ('23:00', '11:30 pm'),
    ('24:00', '12 am'), ('24:00', '12:30 am'),
)

class ProfileModel(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)

    class Meta:
        abstract = True


class Musician(ProfileModel):
    genres = models.ManyToManyField('Genre', blank=True)
    summary = models.TextField(blank=True)
    company = models.CharField(max_length=60, blank=True)
    video = models.ManyToManyField('Video', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    availability = models.ManyToManyField('TimeFrame', blank=True)

    def __str__(self):
        return 'Username: {}'.format(self.user.username)

class NonMusician(ProfileModel):
    summary = models.TextField(blank=True)
    company = models.CharField(max_length=60, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Username: {}'.format(self.user.username)


class Genre(models.Model):
    genre = models.CharField(choices=GENRES, max_length=20)
    description = models.CharField(max_length=140, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.genre)


class Video(models.Model):
    title = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    embedded_code = models.CharField(max_length=20, blank=True)
    upload = models.FileField(upload_to='video/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'video title: {}'.format(self.title)


class TimeFrame(models.Model):
    day = models.CharField(choices=DAYS, max_length=10)
    start = models.CharField(choices=TIMES, max_length=10)
    end = models.CharField(choices=TIMES, max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}-{}'.format(self.day, self.start, self.end)




