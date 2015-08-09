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


def denied(request):
    return render(request, 'main/denied.html')


def musician_current_location_view(request):
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
            radius = user.search_range
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
                            print('loc_o != user')
                            print(loc_o_user.pk)
                            try:
                                print('trying....and...crying')
                                sav = SavedMusician.objects.filter(numbre=loc_o_user.pk)[0]
                                print('im here')
                                try:
                                    print('not....crying..as..bad')
                                    com = Comrade.objects.filter(numbre=sav)[0]
                                    print('Yay you know it worked!')
                                except:
                                    com = Comrade.objects.create(numbre=sav)
                                print('Sav...{}....and....Com...{}...Created in try.....'.format(
                                    sav,
                                    com))
                            except:
                                sav = SavedMusician.objects.create(numbre=loc_o_user.pk)
                                sav.save()
                                com = Comrade.objects.create(numbre=sav)
                                print('Sav...{}....and....Com...{}...Created in except.....'.format(
                                    sav,
                                    com))
                                com.save()
                                print('........{}....SavedMusician....Has Been Saved....You are welcome.... '.format(
                                    loc_o_user))
                            if com in user.comrades.all():
                                print('Com {} already in {}s comrade list'.format(
                                    com,
                                    user))
                                pass
                            else:
                                user.comrades.add(com)
                                user.save()
                                print('....{}...added..to....{}'.format(
                                    com,
                                    user))
                    except:
                        print('......hit.....except...in....current_location_view...')
                        pass
            return redirect('main:feed')


def nonmusician_current_location_view(request):
    if request.POST:
        cor_data = request.POST['coordinates']
        if request.user.nonmusician:
            print('nonmusician ajax works')
            user = request.user.nonmusician
            user.current_location = cor_data
            user.save()
            print('Working NonMusic Loc is {}'.format(user.current_location))
            coor = user.current_location
            lat = float(coor.latitude)
            lon = float(coor.longitude)
            current_location = Point(lon, lat)
            radius = user.search_range
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
                            print('loc_o != user')
                            print(loc_o_user.pk)
                            try:
                                print('trying....and...crying')
                                sav = SavedMusician.objects.filter(numbre=loc_o_user.pk)[0]
                                print('im here')
                                try:
                                    print('not....crying..as..bad')
                                    com = Comrade.objects.filter(numbre=sav)[0]
                                    print('Yay you know it worked!')
                                except:
                                    com = Comrade.objects.create(numbre=sav)
                                print('Sav...{}....and....Com...{}...Created in try.....'.format(
                                    sav,
                                    com))
                            except:
                                sav = SavedMusician.objects.create(numbre=loc_o_user.pk)
                                sav.save()
                                com = Comrade.objects.create(numbre=sav)
                                print('Sav...{}....and....Com...{}...Created in except.....'.format(
                                    sav,
                                    com))
                                com.save()
                                print('........{}....SavedMusician....Has Been Saved....You are welcome.... '.format(
                                    loc_o_user))
                            if com in user.comrades.all():
                                print('Com {} already in {}s comrade list'.format(
                                    com,
                                    user))
                                pass
                            else:
                                user.comrades.add(com)
                                user.save()
                                print('....{}...added..to....{}'.format(
                                    com,
                                    user))
                    except:
                        print('......hit.....except...in....current_location_view...')
                        pass
            return redirect('main:feed')


