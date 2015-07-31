from django.contrib.auth.models import User
from django.db import models
from .choices_list import GENRES, DAYS, TIMES, INSTRUMENT_CLASSES, STATES

# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    email = models.EmailField(blank=True)
    latitude = models.DecimalField(blank=True, null=True, max_digits=200, decimal_places=10)
    longitude = models.DecimalField(blank=True, null=True, max_digits=200, decimal_places=10)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)
    locations = models.ManyToManyField('Location', blank=True)
    is_musician = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Musician(ProfileModel):
    genres = models.ManyToManyField('Genre', blank=True)
    summary = models.TextField(blank=True)
    company = models.CharField(max_length=60, blank=True)
    video = models.ManyToManyField('Video', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    instrument_group = models.ManyToManyField('InstrumentGroup', blank=True)
    availability = models.ManyToManyField('TimeFrame', blank=True)
    friends = models.ManyToManyField('SavedMusician', blank=True)

    def __str__(self):
        return 'Username: {}'.format(self.user.username)

class NonMusician(ProfileModel):
    summary = models.TextField(blank=True)
    company = models.CharField(max_length=60, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    musicians = models.ManyToManyField('SavedMusician', blank=True)

    def __str__(self):
        return 'Username: {}'.format(self.user.username)


class Genre(models.Model):
    user_pk = models.IntegerField(default=-1)
    genre = models.CharField(choices=GENRES, max_length=20)
    description = models.CharField(max_length=140, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.genre, self.description)


class Video(models.Model):
    user_pk = models.IntegerField(default=-1)
    title = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    embedded_code = models.CharField(max_length=20, blank=True)
    upload = models.FileField(upload_to='video/%Y/%m/%d/{}'.format('title'), blank=True)
    genre = models.ManyToManyField('Genre', blank=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.timestamp)

    class Meta:
        ordering = ['-timestamp']


class InstrumentGroup(models.Model):
    user_pk = models.IntegerField(default=-1)
    family = models.CharField(choices=INSTRUMENT_CLASSES, max_length=60)
    description = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.family, self.description)


class TimeFrame(models.Model):
    user_pk = models.IntegerField(default=-1)
    day = models.CharField(choices=DAYS, max_length=10)
    start = models.CharField(choices=TIMES, max_length=10)
    end = models.CharField(choices=TIMES, max_length=10)
    all_day = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}-{}'.format(self.day, self.start, self.end)


class Location(models.Model):
    user_pk = models.IntegerField(default=-1)
    zipcode = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = models.CharField(choices=STATES, blank=True, max_length=2)
    latitude = models.DecimalField(blank=True, max_digits=200, decimal_places=10, null=True)
    longitude = models.DecimalField(blank=True, max_digits=200, decimal_places=10, null=True)

    def __str__(self):
        return '{} {}'.format(self.city, self.state)


class SavedMusician(models.Model):
    musician_pk = models.IntegerField()
