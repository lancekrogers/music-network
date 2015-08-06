from django.conf.urls import include, url
from .views import home, feed, something

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^main-feed/$', feed, name='feed'),
    url(r'^ajax/$', something, name='something'),
]