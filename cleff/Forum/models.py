from autoslug import AutoSlugField
from django.db import models
from profiles.models import Musician, NonMusician
from profiles.choices_list import STATES
from profiles.models import Location
from geoposition.fields import GeopositionField
# Create your models here.


class MusicianPost(models.Model):
    user = models.ForeignKey(Musician)
    title = models.CharField(max_length=140)
    text = models.TextField()
    slug = AutoSlugField(populate_from='title')
    score = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField('Vote', blank=True)
    location = GeopositionField(blank=True)

    def __str__(self):
        return "{}".format(self.title)

    @property
    def upvote_count(self):
        upvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_question=True).filter(upvote=True)
        return upvotes.count()

    @property
    def downvote_count(self):
        downvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_question=True).filter(downvote=True)
        return downvotes.count()

    class Meta:
        ordering = ['-timestamp']



class MusicianResponse(models.Model):
    user = models.ForeignKey(Musician)
    post = models.ForeignKey(MusicianPost)
    text = models.TextField()
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField('Vote', blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '{}'.format(self.post.title)

    @property
    def upvote_count(self):
        upvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_answer=True).filter(upvote=True)
        return upvotes.count()

    @property
    def downvote_count(self):
        downvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_answer=True).filter(downvote=True)
        return downvotes.count()


class NonMusicianPost(models.Model):
    user = models.ForeignKey(NonMusician)
    title = models.CharField(max_length=140)
    text = models.TextField()
    slug = AutoSlugField(populate_from='title')
    score = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField('Vote', blank=True)
    location = GeopositionField(blank=True)

    def __str__(self):
        return "{}, user: {}".format(self.title, self.user.user.username)

    @property
    def upvote_count(self):
        upvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_question=True).filter(upvote=True)
        return upvotes.count()

    @property
    def downvote_count(self):
        downvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_question=True).filter(downvote=True)
        return downvotes.count()

    class Meta:
        ordering = ['-timestamp']


class NonMusicianResponse(models.Model):
    musician = models.ForeignKey(Musician, blank=True, null=True)
    nonmusician = models.ForeignKey(NonMusician, blank=True, null=True)
    post = models.ForeignKey(NonMusicianPost)
    text = models.TextField()
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    votes = models.ManyToManyField('Vote', blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return '{}'.format(self.post.title)

    @property
    def upvote_count(self):
        upvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_answer=True).filter(upvote=True)
        return upvotes.count()

    @property
    def downvote_count(self):
        downvotes = Vote.objects.filter(voter_pk=self.pk).filter(is_answer=True).filter(downvote=True)
        return downvotes.count()


class Tag(models.Model):
    tag = models.CharField(max_length=45) #length of longest english word
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ['-score']

    def __str__(self):
        return '{}'.format(self.tag)


class Vote(models.Model):                               # I plan on handling this by making
    votee_pk = models.IntegerField(default=-1)          # a function in my views.py that
    voter = models.ForeignKey(Musician, default=None)  # will take in **kwargs and will
    upvote = models.BooleanField(default=False)                      # be able to put into context data
    downvote = models.BooleanField(default=False)               # when completed == True vote is active
    completed = models.BooleanField(default=False)  # that function can then be turned
    timestamp = models.DateTimeField(auto_now_add=True)  # into two buttons labeled upvote and downvote
    is_post = models.BooleanField(default=False)  # votee_pk is the model being voted on
    is_response = models.BooleanField(default=False)

    def __str__(self):                            # params will still need to be set based on the
        if self.upvote == True:                   # instance and possibly in the the template
            return 'Upvote'                       # using if statments and for loops
        elif self.downvote == True:
            return 'Downvote'
        else:
            return 'No vote'


