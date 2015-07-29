from __future__ import unicode_literals
from django import forms
from .models import Musician, NonMusician, Video, Location, Genre, InstrumentGroup, TimeFrame

class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Please upload a profile image')


class MusicianForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = ['profile_image',
                  'email',
                  'first_name', 'last_name',
                  'profile_image',
                  'summary', 'company',
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


class NonMusicianForm(forms.ModelForm):

    class Meta:
        model = NonMusician
        fields = ['profile_image',
                  'email', 'first_name',
                  'last_name', 'summary',
                  'company',
                  ]