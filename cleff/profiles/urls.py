from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from .views import musician_registration, non_musician_registration, choose

urlpatterns = [
    url(r'^register-musician/$', musician_registration, name='register_musician'),
    url(r'^register-non-musician/$', non_musician_registration, name='register_non_musician'),
    url(r'^login/', login, name='Login'),
    url(r'^logout/', logout, {'next_page': 'main:home'}, name='Logout'),
    url(r'^choose/$', choose, name='choose')
]
