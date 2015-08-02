from django.db import models
from django.conf import settings
from profiles.models import Musician, NonMusician
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class MusicianMusicianConversation(models.Model):
    initializer = models.ForeignKey(Musician, related_name='initializer')
    musician_one = models.ForeignKey(Musician, related_name='musician_one')
    musician_two = models.ForeignKey(Musician, related_name='musician_two')
    messages = models.ManyToManyField('MusMusMessage', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '{} conversation, started by {}'.format(self.pk, self.initializer)


class MusMusMessage(models.Model):
    message = models.TextField()
    conversation = models.ManyToManyField(MusicianMusicianConversation)
    sender = models.ForeignKey(Musician, related_name='sender')
    receiver = models.ForeignKey(Musician, related_name='receiver')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.conversation, self.timestamp)

    class Meta:
        ordering = ['-timestamp']





