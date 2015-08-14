from django.conf.urls import include, url
from .views import MusicianMusicianConversationListView, \
    MusicianMusicianConversationDetailView, mm_start_conv, \
    mm_message_create_view, conversation_delete

urlpatterns = [
    url(r'^$',
        MusicianMusicianConversationListView.as_view(),
        name='musician_conversations'),
    url(r'^musician-conversation/(?P<pk>\d+)/',
        MusicianMusicianConversationDetailView.as_view(),
        name='musician_conv_detail_view'),
    url(r'^start-music-talk/(?P<receiver_pk>\d+)/',
        mm_start_conv,
        name='start_music_talk'),
    url(r'^musician-musician-message/(?P<conversation_pk>\d+)/(?P<receiver_pk>\d+)/',
        mm_message_create_view,
        name='mm_send_message'),
    url(r'^conversation-delete/(?P<conversation_pk>\d+)/',
        conversation_delete,
        name='message_delete'),
]