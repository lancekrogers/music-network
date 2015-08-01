from django.db import models
from django.conf import settings
from profiles.models import Musician, NonMusician
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class MusicianInbox(models.Model):
    music_one = models.ForeignKey(Musician, related_name='music_one')
    music_two = models.ForeignKey(Musician, related_name='music_two')
    timestamp = models.DateTimeField(auto_now_add=True)

class MusicianMusicianChat(models.Model):
    sender = models.ForeignKey(Musician)
    reciever = models.ForeignKey(Musician)
    timestamp = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    message = models.TextField()
    sender = models.OneToOneField('Musician')
    receiver = models.ForeignKey('Musician')
    timestamp = models.DateTimeField(auto_now_add=True)
