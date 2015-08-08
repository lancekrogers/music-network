from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.models import Musician, Location, TimeFrame, Video, NonMusician, \
    SavedMusician, Comrade
from django.contrib.gis.geos import Point
from haystack.query import SearchQuerySet
from haystack.utils.geo import Distance
# Create your views here.

def home(request):
    return render(request, 'main/home_page.html')


def feed(request):
    return render(request, 'main/main-feed.html')


def current_location_view(request):
    if request.POST:
        cor_data = request.POST['coordinates']
        print(cor_data)
        if request.user.musician:
            print('worked at if')
            user = request.user.musician
            print('still working at if')
            print(user.current_location)
            user.current_location = cor_data
            user.save()
            print('Working Music Loc is {}'.format(user.current_location))
            loca = Location.objects.create(
                user_pk=user.pk,
                location=cor_data,
            )
            loca.save()
            coor = user.current_location
            lat = float(coor.latitude)
            lon = float(coor.longitude)
            current_location = Point(lon, lat)
            radius = request.user.musician.search_range
            max_dist = Distance(mi=radius)
            loc_match = SearchQuerySet().dwithin(
                'location',
                current_location,
                max_dist)
            if len(loc_match) > 0:
                for obj in loc_match:
                    try:
                        loc_o = Location.objects.get(pk=obj.pk)
                        loc_o_user = Musician.objects.get(pk=loc_o.user_pk)
                        if loc_o_user != user:
                            if not loc_o_user in SavedMusician.objects.all():
                                sav = SavedMusician.objects.create(musician_pk=int(loc_o_user.pk))
                                sav.save()
                                com = Comrade.objects.create(musicians=sav)
                                print('Sav...{}....and....Com...{}...Created in if not.....'.format(
                                    sav,
                                    com))
                                com.save()
                                print('........{}....SavedMusician...... '.format(loc_o_user))
                            else:
                                sav = SavedMusician.objects.get(musician_pk=int(loc_o_user.pk))
                                com = Comrade.objects.get(musicians=sav)
                                print('Sav...{}....and....Com...{}...Created in if not.....'.format(
                                    sav,
                                    com))
                            if not com in user.comrades.all():

                                user.comrades.add(com)
                                user.save()
                                print('....{}...added..to....{}'.format(
                                    com,
                                    user.username))
                            else:
                                print()
                    except:
                        print('......hit.....except...in....current_location_view...')
                        pass
            return redirect('main:feed')


def non_current_location_view(request):
    if request.POST:
        cor_data = request.POST['coordinates']
        if request.user.nonmusician:
            print('nonmusician ajax works')
            user = request.user.nonmusician
            user.current_location = cor_data
            user.save()
            print('working nonmusician c_loc {}'.format(cor_data))
            return redirect('main:feed')


def distance_search(request):
    if request.POST:
        if request.user.musician:
            coor = request.user.musician.current_location
            lat = float(coor.latitude)
            lon = float(coor.longitude)
            current_location = Point(lon, lat)
            radius = request.user.musician.search_range
            max_dist = Distance(mi=radius)
            loc_match = SearchQuerySet().dwithin('location', current_location, max_dist)
            print(loc_match)
        elif request.user.nonmusician:
            coor = request.user.current_location
            lat = float(coor.latitude)
            lon = float(coor.longitude)
            current_location = Point(lon, lat)
            radius = request.user.nonmusician.search_range
            max_dist = Distance(mi=radius)
            loc_match = SearchQuerySet().dwithin('location', current_location, max_dist)
            print(loc_match)
        else:
            messages.add_message(request, 20, 'Please Login')
            return redirect('main:feed')
