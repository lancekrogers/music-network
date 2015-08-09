from django.conf.urls import include, url
from .views import home, feed, musician_current_location_view, \
    nonmusician_current_location_view

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^main-feed/$', feed, name='feed'),
    url(r'^current/$', musician_current_location_view, name='current'),
    url(r'^non-music-current/$', nonmusician_current_location_view, name='non_current'),
]