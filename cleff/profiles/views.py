from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, render_to_response, redirect
from .forms import MusicianCreateForm, NonMusicianCreateForm, GenreForm, VideoForm, TimeFrameForm, \
InstrumentGroupForm, LocationForm, ProfileImageForm
from .models import Musician, NonMusician, Video
# Create your views here.
from django.template import RequestContext


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
    return render(request, 'choose.html')


def musician_profile(request, user_id):
    try:
        profile = Musician.objects.get(pk=user_id)
    except Musician.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>')
    if Video.objects.filter(user_pk=user_id):
        videos = Video.objects.filter(user=user_id)
        context = {"profile": profile, 'videos': videos}
    else:
        context = {"profile": profile}
    context['videos'] = Video.objects.filter(user_pk=user_id)
    return render_to_response("musician-profile.html",
                              context, context_instance=RequestContext(request))


def non_musician_profile(request, user_id):
    try:
        profile = NonMusician.objects.get(pk=user_id)
    except NonMusician.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>')
    return render_to_response("non-musician-profile.html", {'profile': profile},
                              context_instance=RequestContext(request))