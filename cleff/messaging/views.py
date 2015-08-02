from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, CreateView
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
        return MusicianMusicianConversation.objects.filter(Q(musician_one=profile) | Q(musician_two=profile))


class MusicianMusicianConversationDetailView(DetailView):
    model = MusicianMusicianConversation
    fields = ['messages']

    def list_of_messages(self):
        return MusicianMusicianConversation.messages

def mm_start_conv(request, reciever_pk):
    me = Musician.objects.get(pk=request.user.pk)
    other = Musician.objects.get(pk=reciever_pk)
    redirection = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        print('post mm_start_conv')
        if not MusicianMusicianConversation.objects.filter(Q(musician_one=me, musician_two=other) |
                                                           Q(musician_one=other, musician_two=me)):
            obj = MusicianMusicianConversation.objects.create(
                initializer=me,
                musician_one=me,
                musician_two=other,
            )
            obj.save()
            return redirect('message:musician_conv_detail_view', obj.pk)
        else:
            obj = MusicianMusicianConversation.objects.get(Q(musician_one=me, musician_two=other) |
                                                           Q(musician_one=other, musician_two=me))
            return redirect('message:musician_conv_detail_view', obj.pk)
    else:
        print('doesnt work')
        return HttpResponseRedirect(redirection)