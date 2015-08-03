from django.conf.urls import url
from .views import MusicianPostListView, musician_post_page, vote_create, non_musician_post_page, \
    NonMusicianPostListView, musician_response_create, MusicianPostCreateView

urlpatterns = [
    url(r'^musician-post/$',
        MusicianPostListView.as_view(),
        name='musician_post_list'),
    url(r'^musician-post/(?P<post_id>\d)/$',
        musician_post_page,
        name='musician_post_detail'),
    url(r'^vote/(?P<votee_pk>\d+)/(?P<model_type>post|response+)/(?P<vote_type>upvote|downvote+)/$',
        vote_create, name='vote_create'),
    url(r'^non-musician-post/$',
        NonMusicianPostListView.as_view(),
        name='non_musician_post_list'),
    url(r'^non-musician-post/(?P<post_id>\d)/$',
        non_musician_post_page,
        name='non_musician_post_detail'),
    url(r'^response-create/(?P<post_id>\d)/',
        musician_response_create,
        name='m_response_create'),
    url(r'^create-musician-post/', MusicianPostCreateView.as_view(), name='create_musician_post'),
]