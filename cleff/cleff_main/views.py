from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import INFO
from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.models import Musician, Location, TimeFrame, Video, NonMusician, \
    SavedMusician, Comrade
from django.contrib.gis.geos import Point
from haystack.query import SearchQuerySet
from haystack.utils.geo import Distance
import random
# Create your views here.

def home(request):
    try:
        if request.user.username.all:
            return redirect('main:feed')
    except:
        return render(request, 'main/home_page.html')


@login_required
def feed(request):
    context = render_comrades(request)
    return render(request, 'main/main-feed.html', context)


def denied(request):
    return render(request, 'main/denied.html')


@login_required
def musician_current_location_view(request):
    if request.POST:
        cor_data = request.POST['coordinates']
        if request.user.musician:
            print('musician ajax worked')
            user = request.user.musician
        #    print('still working at if')
        #    print(user.current_location)
            user.current_location = cor_data
            user.save()
      #      print('Working Music Loc is {}'.format(user.current_location))
            loca = Location.objects.create(
                user_pk=user.pk,
                location=cor_data,
            )
            loca.save()
        #    print('loca {}'.format(loca.user_pk))
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
            com_list = []
            if len(loc_match) > 0:
                for obj in loc_match:
                    try:
                        loc_o = Location.objects.get(pk=obj.pk)
                        loc_o_user = Musician.objects.get(pk=loc_o.user_pk)
                        if loc_o_user != user:
                            try:
                                sav = SavedMusician.objects.filter(numbre=loc_o_user.pk,
                                                                   saver_musician=request.user.musician)[0]
                                try:
                                    com = Comrade.objects.filter(numbre=sav)[0]
                                    com_list.append(com)
                                except:
                                    com = Comrade.objects.create(numbre=sav)
                                    com_list.append(com)
                            except:
                                sav = SavedMusician.objects.create(numbre=loc_o_user.pk,
                                                                   saver_musician=request.user.musician)
                                sav.save()
                                print(sav)
                                com = Comrade.objects.create(numbre=sav)
                                com.save()
                                com_list.append(com)
                            if com in user.comrades.all():
                                print('Com {} already in {}s comrade list'.format(
                                    com,
                                    user))
                                pass
                            else:

                                user.comrades.add(com)
                                user.save()
                    except:
                        pass
                if com_list:
                    for co in user.comrades.all():
                        if co not in com_list:
                            print('should remove {} from {}.comrades'.format(co, user))
                            user.comrades.remove(co)
                else:
                    pass
            return redirect('main:feed')


@login_required
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
            com_list = []
            if len(loc_match) > 0:
                for obj in loc_match:
                    try:
                        loc_o = Location.objects.get(pk=obj.pk)
                        loc_o_user = Musician.objects.get(pk=loc_o.user_pk)
                        if loc_o_user != user:
                            try:
                                sav = SavedMusician.objects.filter(numbre=loc_o_user.pk,
                                                                   saver_nonmusician=request.user.nonmusician)[0]
                                try:
                                    com = Comrade.objects.filter(numbre=sav)[0]
                                    com_list.append(com)
                                except:
                                    com = Comrade.objects.create(numbre=sav)
                                    com_list.append(com)
                            except:
                                sav = SavedMusician.objects.create(numbre=loc_o_user.pk,
                                                                   saver_nonmusician=request.user.nonmusician)
                                sav.save()
                                com = Comrade.objects.create(numbre=sav)
                                com.save()
                                com_list.append(com)
                            if com in user.comrades.all():
                                pass
                            else:
                                user.comrades.add(com)
                                user.save()
                    except:
                        pass
                if com_list:
                    print('1 n')
                    count = 2
                    for co in user.comrades.all():
                        print('{} n'.format(count))
                        count += 1
                        if co not in com_list:
                            print('should remove {} from {}.comrades'.format(co, user))
                            user.comrades.remove(co)
                else:
                    print('wowzer')
                    pass
            return redirect('main:feed')


@login_required
def render_comrades(request):
    print('...........render..comrades.........')
    context = {}
    try:
        print('.......render_comrades ...is..musician....')
        visitor = request.user.musician
        comrades = visitor.comrades.all()
        musician_list = []
        try:
            for com in reversed(comrades):
                muc = Musician.objects.get(pk=com.numbre.numbre)
                musician_list.append(muc)
        except:
            messages.add_message(request, 20, 'No Musician Matches')
        context['comrades'] = musician_list
    except:
        print('......non..musician.....render.....comrades...')
        visitor = request.user.nonmusician
        comrades = visitor.comrades.all()
        musician_list = []
        try:
            for com in comrades:
                muc = Musician.objects.get(pk=com.numbre.numbre)
                musician_list.append(muc)
        except:
            messages.add_message(request, 20, 'No Musician Matches')
        context['comrades'] = musician_list
    return context


