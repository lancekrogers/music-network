from django.http import HttpResponse
from django.shortcuts import render, redirect
from profiles.models import Musician, Location
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
            print('Working Music Loc is {}'.format(user.current_location))
        elif request.user.nonmusician:
            print('worked at elif')
            user = request.user.nonmusician
            user.current_location = cor_data
            print('Working NonMusic Loc is {}'.format(user.current_location))
            user.save()
        else:
            # this doesnt work yet
            print('made it to else')
            temp = cor_data.split(',', 2)
            lat = temp[0]
            lon = temp[1]
            print('session func does work {}-{}'.format(lon, lat))
            request.session['current_location'] = {
                'latitude': lat,
                'longitude': lon,
            }

        return redirect('main:feed')