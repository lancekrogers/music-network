from __future__ import unicode_literals
from django import forms
from .models import Musician, NonMusician, Video, Location, Genre, InstrumentGroup, TimeFrame
from .choices_list import *


class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Please upload a profile image', required=False)


class MusicianUpdateForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = [
            'email',
            'first_name',
            'last_name',
            'summary'
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


class TimeFrameForm(forms.ModelForm):

    class Meta:
        model = TimeFrame
        fields = [
            'day',
            'start',
            'end',
        ]


class NonMusicianCreateForm(forms.ModelForm):

    class Meta:
        model = NonMusician
        fields = [
                 'email'
                  ]