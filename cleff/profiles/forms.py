from __future__ import unicode_literals
from django import forms
from .models import Musician, NonMusician, Video, Location, Genre, InstrumentGroup, TimeFrame
from .choices_list import *

class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Please upload a profile image', required=False)

class YoutubeUrlForm(forms.Form):
    youtube = forms.CharField(max_length=43)
                              #verbose_name="To post a video: 1. Upload a video on youtube.\n2. Copy video url from your\
                              # browser\n3. Paste your videos url here\n4. Hit 'Post Video'")

class MusicianUpdateForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = [
            'email',
            'first_name',
            'last_name',
            'summary',
            'company',
                  ]
        required = False


class MusicianCreateForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = [
            'email'
        ]


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = [
            'title',
            'embedded_code',
            'upload',
        ]


class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = [
            'zipcode',
            'city',
        ]


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = [
            'genre',
            'description',
        ]


class InstrumentGroupForm(forms.ModelForm):

    class Meta:
        model = InstrumentGroup
        fields = [
            'family',
            'description'
        ]


class TimeFrameForm(forms.Form):
    # you need to figure out how to alter x after start_time or end_time are selected
    # I was thinking pop anything out of x that is before start time, and if end_time is
    # selected first pop anythin out of x that is after the selected end_time
    x = TIMES
    day = forms.ChoiceField(choices=DAYS)
    start_time = forms.ChoiceField(choices=x)
    end_time = forms.ChoiceField(choices=x)


class NonMusicianCreateForm(forms.ModelForm):

    class Meta:
        model = NonMusician
        fields = ['email']


class NonMusicianUpdateForm(forms.ModelForm):

    class Meta:
        model = NonMusician
        fields = [
            'email',
            'company',
            'summary'
        ]