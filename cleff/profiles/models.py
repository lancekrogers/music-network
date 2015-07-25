from django.contrib.auth.models import User
from django.db import models

# Create your models here.


GENRES = [
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

]

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




