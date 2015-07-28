from __future__ import unicode_literals
from django import forms
from .models import Musician, NonMusician

class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Please upload a profile image')


class MusicianForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = ['profile_image',
                  'video',
                  'locations', 'email',
                  'genres', 'instrument_group',
                  'availability',
                  'first_name', 'last_name',
                  'summary', 'company',
                  ]


class NonMusicianForm(forms.ModelForm):

    class Meta:
        model = NonMusician
        fields = ['profile_image',
                  'locations', 'email',
                  'first_name', 'last_name',
                  'summary', 'company',
                  ]