from django.conf.urls import include, url
from .views import MusicianMusicianConversationListView



urlpatterns = [
    url(r'^musician-conversations/', MusicianMusicianConversationListView.as_view(), name='musician_conversations')
]