from django.conf.urls import include, url
from .views import MusicianMusicianConversationListView, MusicianMusicianConversationDetailView, mm_start_conv

urlpatterns = [
    url(r'^$',
        MusicianMusicianConversationListView.as_view(),
        name='musician_conversations'),
    url(r'^musician-conversation/(?P<pk>\d)',
        MusicianMusicianConversationDetailView.as_view(),
        name='musician_conv_detail_view'),
    url(r'start-music-talk/(?P<reciever_pk>\d)',
        mm_start_conv,
        name='start_music_talk'),
]