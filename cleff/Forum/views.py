import random
from django.shortcuts import render, redirect
from profiles.models import Musician, NonMusician
from .models import Vote, MusicianPost, MusicianResponse
# Create your views here.

def vote_create(request, votee_pk, model_type, vote_type='upvote'):
    print('here') # separate this out into more than one function so that
    x_var = votee_pk    # people can only vote on one question at a time
    if request.POST:
        print('sent post')
        user_pk = request.user.pk
        profile = Musician.objects.get(pk=user_pk)
        if not Vote.objects.filter(votee_pk=votee_pk).filter(voter=profile):
            musician_post = False
            answer = False
            downvote = False
            upvote = True
            model_type = model_type
            obj = ''
            if model_type == 'musician_post':
                musician_post = True
                obj = MusicianPost.objects.get(pk=votee_pk)
            if model_type == 'musician_response':
                answer = True
                obj = MusicianResponse.objects.get(pk=votee_pk)
                x_var = obj.question.pk
            if vote_type == 'downvote':
                downvote = True
                upvote = False
                obj.score -= 5
                obj.save()
            else:
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
        return redirect('Forum:musician_post_page', musician_post_id=x_var)
    else:
       return redirect('Forum:musician_post_page', musician_post_id=x_var)