"""cleff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings

from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
                  #  url('', include('social.apps.django_app.urls', namespace='social')),
                  #  url('', include('django.contrib.auth.urls', namespace='auth')),
                  url(r'^admin/',
                      include(admin.site.urls)),
                  url(r'^profiles/',
                      include('profiles.urls',
                              namespace='profiles')),
                  url(r'^forum/',
                      include('Forum.urls',
                              namespace='Forum')),
                  url(r'^',
                      include('cleff_main.urls', namespace='main')),
                  url(r'^uploads/',
                      include('stickyuploads.urls')),
                  url(r'^message/',
                      include('messaging.urls',
                              namespace='message')),
                  url(r'^search/',
                      include('haystack.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
