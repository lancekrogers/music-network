from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from .views import home, musician_registration, non_musician_registration

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register-musician/$', musician_registration, name='register_musician'),
    url(r'^register-non-musician/$', non_musician_registration, name='register_non_musician'),
    url(r'^login/', login, name='Login'),
    url(r'^logout/', logout, {'next_page': 'profiles:home'}, name='Logout'),
]