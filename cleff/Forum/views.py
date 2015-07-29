from django.shortcuts import render
from profiles.models import Musician, NonMusician
from .models import Vote, MusicianPost, MusicianResponse
# Create your views here.

def vote_create(request, votee_pk, model_type, vote_type='upvote'):
    print('here') # separate this out into more than one function so that
    x_var = votee_pk    # people can only vote on one question at a time
    if request.POST:
        print('sent post')
        user_pk = request.user.pk
        musician_post = False
        answer = False
        downvote = False
        upvote = True
        profile = Musician.objects.get(pk=user_pk)
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
            numset = '000000001'
            if profile.score < 25:
                numset = '010021'
            rand = random.choice(numset)
            owner = Profile.objects.get(pk=obj.user.pk)
            owner.score += 10
            print('It works here is the owners score:', owner.score)
            profile.score += int(rand)
            profile.save()
            obj.score += 10
            obj.save()
            owner.save()
        vote = Vote.objects.create(votee_pk=votee_pk,
                                   voter=profile,
                                   upvote=upvote,
                                   downvote=downvote,
                                   completed=True,
                                   is_question=question,
                                   is_answer=answer)
        vote.save()
        return redirect('stack:question_page', question_id=x_var)
    else:
       return redirect('stack:question_page', question_id=x_var)