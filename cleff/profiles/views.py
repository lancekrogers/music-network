from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages import INFO
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.utils.datastructures import MultiValueDictKeyError
from .forms import MusicianCreateForm, NonMusicianCreateForm, GenreForm, VideoForm, TimeFrameForm, \
InstrumentGroupForm, LocationForm, ProfileImageForm, MusicianUpdateForm, MusicianUpdateAvailabilityForm, \
    UpdateGenresForm, UpdateInstrumentsForm, UpdateLocationsForm, YoutubeUrlForm, UpdateVideoForm, UpdateFriendsForm, \
    NonMusicianUpdateForm, NonMusicianUpdateWatchedMusicians
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Musician, NonMusician, Video, TimeFrame, Genre, InstrumentGroup, Location
# Create your views here.
from django.template import RequestContext
from profiles.choices_list import TIMES, DAYS
from random_functions import youtube_code_getter




def musician_registration(request):
    print('first print')
    if request.POST:
        print('second print')
        ok = True
        m_form = MusicianCreateForm(request.POST)
        user_creation_form = UserCreationForm(request.POST)
        print('third print')
        if not user_creation_form.is_valid():
            print('4th print')
            ok = False
        if not m_form.is_valid():
            print('5th print')
            ok = False
        if ok:
            print('it should work')
            try:
                print('I dont hate my life')
                users = user_creation_form.save()
                profile = m_form.save(commit=False)
                profile.is_musician = True
                profile.user = users
                profile.save()
                try:
                    username = request.POST['username']
                    password = request.POST['password1']
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('main:home')
                except:
                    return redirect('profiles:Login')
            except:
                print('somethings wrong')
                return render_to_response("registration/register_musician.html",
                                      {'u_form': UserCreationForm,
                                       'm_form': MusicianCreateForm},
                                       context_instance=RequestContext(request))
    return render_to_response("registration/register_musician.html",
                                  {'u_form': UserCreationForm,
                                   'm_form': MusicianCreateForm},
                                  context_instance=RequestContext(request))


# add login required later
def non_musician_registration(request):
    print('first non m print')
    if request.POST:
        print('second non m print')
        ok = True
        m_form = NonMusicianCreateForm(request.POST)
        user_creation_form = UserCreationForm(request.POST)
        print('non m third print')
        if not user_creation_form.is_valid():
            print('non m 4th print')
            ok = False
        if not m_form.is_valid():
            print('5th print')
            ok = False
        if ok:
            print('it should work')
            try:
                print('I dont hate my life non m')
                users = user_creation_form.save()
                profile = m_form.save(commit=False)
                profile.is_musician = False
                profile.user = users
                profile.save()
                try:
                    username = request.POST['username']
                    password = request.POST['password1']
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('main:home')
                except:
                    return redirect('profiles:Login')
            except:
                print('somethings wrong non m')
                return render_to_response("registration/register_non_musician.html",
                                      {'u_form': UserCreationForm,
                                       'non_m_form': NonMusicianCreateForm},
                                      context_instance=RequestContext(request))
    return render_to_response("registration/register_non_musician.html",
                                  {'u_form': UserCreationForm,
                                   'non_m_form': NonMusicianCreateForm},
                                  context_instance=RequestContext(request))


def choose(request):
    return render(request, 'profiles/choose.html')


def musician_profile(request, user_id):
    try:
        profile = Musician.objects.get(pk=user_id)
    except Musician.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>')
    if Video.objects.filter(user_pk=user_id):
        videos = Video.objects.filter(user_pk=user_id)
        context = {"profile": profile, 'videos': videos}
    else:
        context = {"profile": profile}
    context['videos'] = Video.objects.filter(user_pk=user_id)
    return render_to_response("profiles/musician-profile.html",
                              context, context_instance=RequestContext(request))


def non_musician_profile(request, user_id):
    try:
        profile = NonMusician.objects.get(pk=user_id)
    except NonMusician.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>')
    return render_to_response("profiles/non-musician-profile.html", {'profile': profile},
                              context_instance=RequestContext(request))


def update_musician_profile(request):
    musician = Musician.objects.get(user=request.user)
    profile = musician
    update_musician_form = MusicianUpdateForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if update_musician_form.is_valid():
            update_musician_form.save()
            print('I am here')
            messages.add_message(request, INFO, 'Profile updated!')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'update_musician': update_musician_form}
    return render(request, 'updates/music-update-profile.html', context)


def update_non_musician_profile(request):
    nonmusician = NonMusician.objects.get(user=request.user)
    profile = nonmusician
    update_nonmusician_form = NonMusicianUpdateForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if update_nonmusician_form.is_valid():
            update_nonmusician_form.save()
            print('I am here')
            messages.add_message(request, INFO, 'Profile updated!')
            return redirect('profiles:non_musician_profile', request.user.pk)
    context = {'update_non_musician': update_nonmusician_form}
    return render(request, 'updates/nonmusic-update-profile.html', context)


def musician_add_time_frame(request):
    musician = Musician.objects.get(user=request.user)
    time_frame_form = TimeFrameForm(request.POST)
    if request.method == 'POST':
        if time_frame_form.is_valid():
            obj = TimeFrame.objects.create(user_pk=request.user.pk,
                                           day=time_frame_form['day'].value(),
                                           start=time_frame_form['start_time'].value(),
                                           end=time_frame_form['end_time'].value(),)
            print('time frame form saved')
            if not Musician.objects.filter(availability=obj).filter(pk=request.user.pk):
                musician.availability.add(obj)
                musician.save()
                messages.add_message(request, INFO, 'Availability added!')
                print('Time frame form should have been added to the musician')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'time_frame_form': time_frame_form}
    return render(request, 'updates/time-frame.html', context)

def musician_update_time_frame(request):
    musician = Musician.objects.get(user=request.user)
    update_musician_form = MusicianUpdateAvailabilityForm(
        request.POST or None,
        instance=musician
    )
    update_musician_form.fields["availability"].queryset = musician.availability.all()
    if request.method == 'POST':
        if update_musician_form.is_valid():
            update_musician_form.save()
            print('I am here')
            messages.add_message(request, INFO, 'Availability updated!')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'update_availability': update_musician_form}
    return render(request, 'updates/music-update-availability.html', context)


def add_genre(request):
    musician = Musician.objects.get(user=request.user)
    genre_form = GenreForm(request.POST)
    if request.method == 'POST':
        if genre_form.is_valid():
            obj = Genre.objects.create(user_pk=request.user.pk,
                genre=genre_form['genre'].value(),
                description=genre_form['description'].value()
            )
            print('genre form saved')
            if not Musician.objects.filter(genres=obj).filter(pk=request.user.pk):
                musician.genres.add(obj)
                musician.save()
                messages.add_message(request, INFO, 'Genre added!')
                print('Genre form should have been added to the musician')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'add_genre_form': genre_form}
    return render(request, 'updates/add-genre.html', context)


def update_genres(request):
    musician = Musician.objects.get(user=request.user)
    update_genres_form = UpdateGenresForm(
        request.POST or None,
        instance=musician
    )
    update_genres_form.fields["genres"].queryset = musician.genres.all()
    if request.method == 'POST':
        if update_genres_form.is_valid():
            update_genres_form.save()
            messages.add_message(request, INFO, 'Genre updated!')
            print('I am here')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'update_genres_form': update_genres_form}
    return render(request, 'updates/update-genres.html', context)


def add_instrument(request):
    musician = Musician.objects.get(user=request.user)
    instrument_form = InstrumentGroupForm(request.POST)
    if request.method == 'POST':
        if instrument_form.is_valid():
            obj = InstrumentGroup.objects.create(user_pk=request.user.pk,
                family=instrument_form['family'].value(),
                description=instrument_form['description'].value()
            )
            print('instrument form saved')
            if not Musician.objects.filter(instrument_group=obj).filter(pk=request.user.pk):
                musician.instrument_group.add(obj)
                musician.save()
                messages.add_message(request, INFO, 'Instrument Family Added!')
                print('Instrument form should have been added to the musician')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'add_instrument_form': instrument_form}
    return render(request, 'updates/add-instrument.html', context)


def update_instruments(request):
    musician = Musician.objects.get(user=request.user)
    update_instruments_form = UpdateInstrumentsForm(
        request.POST or None,
        instance=musician
    )
    update_instruments_form.fields["instrument_group"].queryset = musician.instrument_group.all()
    if request.method == 'POST':
        if update_instruments_form.is_valid():
            update_instruments_form.save()
            messages.add_message(request, INFO, 'Instruments updated!')
            print('I am here')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'update_instruments_form': update_instruments_form}
    return render(request, 'updates/update-instruments.html', context)


def musician_add_location(request):
    musician = Musician.objects.get(user=request.user)
    location_form = LocationForm(request.POST)
    if request.method == 'POST':
        if location_form.is_valid():
            obj = Location.objects.create(user_pk=request.user.pk,
                state=location_form['state'].value(),
                city=location_form['city'].value()
            )
            print('location form saved')
            if not Musician.objects.filter(locations=obj).filter(pk=request.user.pk):
                musician.locations.add(obj)
                musician.save()
                print('Location form should have been added to the musician')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'musician_location_form': location_form}
    return render(request, 'updates/add-musician-location.html', context)


def update_musician_location(request):
    musician = Musician.objects.get(user=request.user)
    update_location_form = UpdateLocationsForm(
        request.POST or None,
        instance=musician
    )
    update_location_form.fields["locations"].queryset = musician.locations.all()
    if request.method == 'POST':
        if update_location_form.is_valid():
            update_location_form.save()
            print('I am after the second if in update musician location')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'update_location_form': update_location_form}
    return render(request, 'updates/update-musician-location.html', context)


def youtube_url_decoder_view(request):
    musician = Musician.objects.get(user=request.user)
    youtube_url_form = YoutubeUrlForm(request.POST)
    data = youtube_url_form['youtube_url'].value()
    if request.method == 'POST':
        if "www.youtube.com/watch?v=" in data:
            if youtube_url_form.is_valid():
                title = youtube_url_form['title'].value()
                genres = youtube_url_form['genre'].value()
                tube_url = youtube_url_form['youtube_url'].value()
                youtube_code = youtube_code_getter(tube_url)
                print(genres)
                obj = Video.objects.create(
                    user_pk=request.user.pk,
                    title=title,
                    embedded_code=youtube_code
                )
                for gen in genres:
                    obj_g = Genre.objects.create(user_pk=request.user.pk,
                                                 genre=gen)
                    obj.genre.add(obj_g)
                obj.save()
                musician.video.add(obj)
                musician.save()
                return redirect('profiles:musician_profile', request.user.pk)
            # figure out how to raise error message here
        else:
            messages.add_message(request, INFO, 'Please enter a Youtube video url!')
    context = {'youtube_url_form': youtube_url_form}
    return render(request, 'updates/add-video.html', context)


def update_video(request):
    musician = Musician.objects.get(user=request.user)
    update_video_form = UpdateVideoForm(
        request.POST or None,
        instance=musician
    )
    update_video_form.fields["video"].queryset = musician.video.all()
    if request.method == 'POST':
        if update_video_form.is_valid():
            update_video_form.save()
            print('I am after the second if in update musician location')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'update_video_form': update_video_form}
    return render(request, 'updates/update-video.html', context)


def update_friends(request):
    musician = Musician.objects.get(user=request.user)
    update_friends_form = UpdateFriendsForm(
        request.POST or None,
        instance=musician
    )
    update_friends_form.fields["friends"].queryset = musician.friends.all()
    if request.method == 'POST':
        if update_friends_form.is_valid():
            update_friends_form.save()
            print('I am after the second if in update musician friends')
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'update_friends_form': update_friends_form}
    return render(request, 'updates/update-friends.html', context)


def add_profile_image(request):
    musician = Musician.objects.get(user=request.user)
    profile_image_form = ProfileImageForm(request.POST, request.FILES)
    print('.......image....user..{}....'.format(request.user.username))
    if request.method == 'POST':
        if profile_image_form.is_valid():
            try:
                musician.profile_image = request.FILES['image']
                musician.save()
                messages.add_message(request, INFO, 'Profile Photo Is Uploading')
                print(request.user.musician.profile_image.url)
            except MultiValueDictKeyError:
                print('MultiValueDictKeyError in add_profile_image')
                messages.add_message(request, INFO, 'Profile Photo Not Updated')
            print(request.user.musician.profile_image.url)
            return redirect('profiles:musician_profile', request.user.pk)
    context = {'profile_image_form': profile_image_form}
    return render(request, 'updates/add-profile-photo.html', context)


def add_profile_image_non_musician(request):
    nonmusician = NonMusician.objects.get(user=request.user)
    profile_image_form = ProfileImageForm(request.POST, request.FILES)
    print('.......image....user..{}....'.format(request.user.username))
    if request.method == 'POST':
        if profile_image_form.is_valid():
            try:
                nonmusician.profile_image = request.FILES['image']
                nonmusician.save()
                messages.add_message(request, INFO, 'Profile Photo Is Uploading')
                print(request.user.nonmusician.profile_image.url)
            except MultiValueDictKeyError:
                print('MultiValueDictKeyError in add_profile_image')
                messages.add_message(request, INFO, 'Profile Photo Not Updated')
            print(request.user.nonmusician.profile_image.url)
            return redirect('profiles:non_musician_profile', request.user.pk)
    context = {'profile_image_form': profile_image_form}
    return render(request, 'updates/non-musician-p-image.html', context)


def update_watched_musicians(request):
    non_musician = NonMusician.objects.get(user=request.user)
    update_watched_form = NonMusicianUpdateWatchedMusicians(
        request.POST or None,
        instance=non_musician,
    )
    update_watched_form.fields["musicians"].queryset = non_musician.musicians.all()
    if request.method == 'POST':
        if update_watched_form.is_valid():
            update_watched_form.save()
            messages.add_message(request, INFO, 'Watched Musicians Updated')
            print('I am after the second if in update musician friends')
            return redirect('profiles:non_musician_profile', request.user.pk)
    context = {'update_watched_form': update_watched_form}
    return render(request, 'updates/update-watched-musicians.html', context)