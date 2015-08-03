from django.conf.urls import url
from .views import MusicianPostListView, musician_post_page, vote_create

urlpatterns = [
    url(r'^musician-post/$',
        MusicianPostListView.as_view(),
        name='musician_post_list'),
    url(r'^musician-post/(?P<post_id>\d)/$',
        musician_post_page,
        name='musician_post_detail'),
    url(r'^vote/(?P<votee_pk>\d+)/(?P<model_type>post|response+)/(?P<vote_type>upvote|downvote+)/$',
        vote_create, name='vote_create'),

]