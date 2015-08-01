from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from profiles.models import Musician
from .models import MusicianMusicianConversation, MusMusMessage
# Create your views here.


class MusicianMusicianConversationListView(ListView):
    model = MusicianMusicianConversation

    def owner_is_musician_one(self):
        owner = Musician.objects.get(pk=self.request.user.pk)
        return MusicianMusicianConversation.objects.filter(musician_one=owner)

    def owner_is_musician_two(self):
        owner = Musician.objects.get(pk=self.request.user.pk)
        return MusicianMusicianConversation.objects.filter(musician_two=owner)

    def get_queryset(self):
        profile = Musician.objects.get(user=self.request.user)
        return MusicianMusicianConversation.objects.filter(Q(musician_one=profile)|Q(musician_two=profile))




