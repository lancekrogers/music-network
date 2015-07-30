from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from .views import musician_registration, non_musician_registration, choose, musician_profile, \
    non_musician_profile, update_musician_profile, musician_add_time_frame, musician_update_time_frame, add_genre,\
    update_genres, add_instrument

urlpatterns = [
    url(r'^register-musician/$', musician_registration, name='register_musician'),
    url(r'^register-non-musician/$', non_musician_registration, name='register_non_musician'),
    url(r'^login/', login, name='Login'),
    url(r'^logout/', logout, {'next_page': 'main:home'}, name='Logout'),
    url(r'^choose/$', choose, name='choose'),
    url(r'^musician/(?P<user_id>\d+)/$', musician_profile, name='musician_profile'),
    url(r'^non-musician/(?P<user_id>\d+)/$', non_musician_profile, name='non_musicain_profile'),
    url(r'^musician/update/$', update_musician_profile, name='musician_update'),
    url(r'^add-availability/', musician_add_time_frame, name='add_availability'),
    url(r'^update-availability/', musician_update_time_frame, name='update_availability'),
    url(r'^add-genre/', add_genre, name='add_genre'),
    url(r'^update-genre/', update_genres, name='update_genres'),
    url(r'^add-family/', add_instrument, name='add_instrument')


]
