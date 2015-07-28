from __future__ import unicode_literals
from django import forms
from .models import Musician, NonMusician

class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Please upload a profile image')


class MusicianForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = ['email', 'first_name',
                  'last_name', 'profile_image',
                  'genres', 'summary',
                  ''
                  ]