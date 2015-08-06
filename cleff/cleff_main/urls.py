from django.conf.urls import include, url
from .views import home, feed, current_location_view

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^main-feed/$', feed, name='feed'),
    url(r'^current/$', current_location_view, name='current'),

]