from django.conf.urls import url
from .views import MusicianPostListView, musician_post_page, vote_create, non_musician_post_page, \
    NonMusicianPostListView, musician_response_create, musician_post_create_view, \
    non_musician_post_response_create, non_musician_post_create_view

urlpatterns = [
    url(r'^$',
        MusicianPostListView.as_view(),
        name='musician_post_list'),
    url(r'^musician-post/(?P<post_id>\d+)/$',
        musician_post_page,
        name='musician_post_detail'),
    url(r'^vote/(?P<votee_pk>\d+)/(?P<model_type>post|response+)/(?P<vote_type>upvote|downvote+)/$',
        vote_create, name='vote_create'),
    url(r'^non-musician-post/$',
        NonMusicianPostListView.as_view(),
        name='non_musician_post_list'),
    url(r'^non-musician-post/(?P<post_id>\d+)/$',
        non_musician_post_page,
        name='non_musician_post_detail'),
    url(r'^response-create/(?P<post_id>\d+)/',
        musician_response_create,
        name='m_response_create'),
    url(r'^create-musician-post/',
        musician_post_create_view,
        name='create_musician_post'),
    url(r'^non-musician-response-create/(?P<post_id>\d+)/$',
        non_musician_post_response_create,
        name='non_m_response_create'),
    url(r'^create-non-musician-post/',
        non_musician_post_create_view,
        name='create_non_musician_post'),
]