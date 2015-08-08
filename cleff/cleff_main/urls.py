from django.conf.urls import include, url
from .views import home, feed, current_location_view, distance_search, \
    non_current_location_view

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^main-feed/$', feed, name='feed'),
    url(r'^current/$', current_location_view, name='current'),
    url(r'^non-music-current/$', non_current_location_view, name='non_current'),
    url(r'^update-queryset/', distance_search, name='distance_search'),
]