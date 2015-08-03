import random
from django.contrib import messages
from django.contrib.messages import INFO
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView
from profiles.models import Musician, NonMusician
from .models import Vote, MusicianPost, MusicianResponse, NonMusicianPost, NonMusicianResponse
from .forms import MusicianResponseForm
# Create your views here.

def vote_create(request, votee_pk, model_type, vote_type='upvote'):
    print('here')  # separate this out into more than one function so that
    if model_type == 'response':
                obj = MusicianResponse.objects.get(pk=votee_pk)
                x_var = obj.post.pk
    else:
        x_var = votee_pk
    if request.POST:
        print('sent post')
        user_pk = request.user.pk
        profile = Musician.objects.get(pk=user_pk)
        if not Vote.objects.filter(votee_pk=votee_pk).filter(voter=profile):
            print('under not')
            musician_post = False
            answer = False
            downvote = False
            upvote = True
            model_type = model_type
            if model_type == 'response':
                obj = MusicianResponse.objects.get(pk=votee_pk)
                answer = True
            if model_type == 'post':
                musician_post = True
                obj = MusicianPost.objects.get(pk=votee_pk)
            if vote_type == 'downvote':
                downvote = True
                upvote = False
                obj.score -= 5
                obj.save()
                vote = Vote.objects.create(votee_pk=votee_pk,
                                       voter=profile,
                                       upvote=upvote,
                                       downvote=downvote,
                                       completed=True,
                                       is_post=musician_post,
                                       is_response=answer)
                vote.save()

            else:
                obj = MusicianResponse.objects.get(pk=votee_pk)
                obj.score += 10
                obj.save()
                vote = Vote.objects.create(votee_pk=votee_pk,
                                       voter=profile,
                                       upvote=upvote,
                                       downvote=downvote,
                                       completed=True,
                                       is_post=musician_post,
                                       is_response=answer)
                vote.save()
        else:
            pass
        return redirect('Forum:musician_post_detail', post_id=x_var)
    else:
        return redirect('Forum:musician_post_detail', post_id=x_var)


class MusicianPostListView(ListView):
    model = MusicianPost


def musician_post_page(request, post_id):
    try:
        ques = MusicianPost.objects.get(pk=post_id)
        if MusicianResponse.objects.filter(post=ques):
            answer = MusicianResponse.objects.filter(post=ques)
            context = {'post': ques, 'response': answer}

        else:
            context = {'post': ques}
    except MusicianPost.DoesNotExist:
        return HttpResponse('Not Found!')
    return render_to_response('Forum/musician_post_detail.html',
                              context,
                              context_instance=RequestContext(request))



class NonMusicianPostListView(ListView):
    model = NonMusicianPost


def non_musician_post_page(request, post_id):
    try:
        ques = NonMusicianPost.objects.get(pk=post_id)
        if NonMusicianResponse.objects.filter(post=ques):
            answer = NonMusicianResponse.objects.filter(post=ques)
            context = {'post': ques, 'response': answer}
        else:
            context = {'post': ques}
    except NonMusicianPost.DoesNotExist:
        return HttpResponse('Not Found!')
    return render_to_response('Forum/non_musician_post_detail.html',
                              context,
                              context_instance=RequestContext(request))


class MusicianCreatePost(CreateView):
    model = MusicianPost
    fields = ['title', 'text', 'location']


class NonMusicianCreatePost(CreateView):
    model = NonMusicianPost
    fields = ['title', 'text']


def musician_response_create(request, post_id):
    print('here')  # separate this out into more than one function so that
    x_var = post_id
    the_post = MusicianPost.objects.get(pk=post_id)
    if request.POST:
        print('sent post m response create')
        user_pk = request.user.pk
        profile = Musician.objects.get(pk=user_pk)
        m = MusicianResponse.objects.create(
            user=profile,
            post=the_post,
            text=request.POST['this'],
        )
        m.save()
        print('mtheory')
        return redirect('Forum:musician_post_detail', post_id=x_var)
    else:
        pass
    return redirect('Forum:musician_post_detail', post_id=x_var)






