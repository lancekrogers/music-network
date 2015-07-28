from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from .forms import MusicianForm, NonMusicianForm
# Create your views here.
from django.template import RequestContext


def user_registration(request):
    if request.POST:
        ok = True
        user_creation_form = UserCreationForm(request.POST)
        if not user_creation_form.is_valid():
            ok = False
        if ok:
            print('it should work')
            try:
                user_creation_form.save()
                return redirect('profiles:login')
            except:
                return render_to_response("registration/create_user.html",
                                      {'u_form': UserCreationForm},
                                      context_instance=RequestContext(request))
    return render_to_response("registration/create_user.html",
                                  {'u_form': UserCreationForm},
                                  context_instance=RequestContext(request))

# add login required
def musician_registration(request):
    if request.POST:
        ok = True
        profile_form = MusicianForm(request.POST)
        if not profile_form.is_valid():
            ok = False
        if not request.user:
            ok = False
        if ok:
            print('Muscian form should work')
            user = request.user
            try:
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('profiles:home')  # add a homepage in forum app
            except:
                return render_to_response('registration/register_musician.html',
                                          {'musician_form': MusicianForm},
                                          context_instance=RequestContext(request))
    return render_to_response('registration/register_musician.html',
                              {'musician_form': MusicianForm},
                              context_instance=RequestContext(request))

# add login required later
def non_musician_registration(request):
    if request.POST:
        ok = True
        profile_form = NonMusicianForm(request.POST)
        if not profile_form.is_valid():
            ok = False
        if not request.user:
            ok = False
        if ok:
            print('NonMuscian form should work')
            user = request.user
            try:
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('profiles:home')  # add a homepage in forum app
            except:
                return render_to_response('registration/register_non_musician.html',
                                          {'non_musician_form': NonMusicianForm},
                                          context_instance=RequestContext(request))
    return render_to_response('registration/register_non_musician.html',
                              {'non_musician_form': NonMusicianForm},
                              context_instance=RequestContext(request))

def home(request):
    return HttpResponse('It worked')