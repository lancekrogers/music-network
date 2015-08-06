from __future__ import unicode_literals
from django import forms
from .models import Musician, NonMusician, Video, Location, Genre, InstrumentGroup, TimeFrame
from .choices_list import *
from stickyuploads.widgets import StickyUploadWidget
from geoposition.fields import GeopositionField
from geoposition.widgets import MapOnlyWidget
from PIL import Image



class ProfileImageForm(forms.Form):
    image = forms.ImageField(label='Please upload a profile image',
                            required=False,
                            widget=StickyUploadWidget,
                            error_messages={'invalid_file': 'Please upload an image'}
                            )

class YoutubeUrlForm(forms.Form):
    title = forms.CharField(max_length=20)
    youtube_url = forms.URLField(max_length=43, error_messages={'not_url': "Not a valid youtube url"})
    genre = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=GENRES)

class UpdateVideoForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = ['video']
        widgets = {'video': forms.CheckboxSelectMultiple}


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


class LocationForm(forms.Form):
    state_list = STATES
    city = forms.CharField(max_length=30)
    state = forms.ChoiceField(choices=state_list)
    location = GeopositionField(blank=True)



class UpdateLocationsForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = ['locations']
        widgets = {'locations': forms.CheckboxSelectMultiple}


class GenreForm(forms.Form):
    choice_list = GENRES
    genre = forms.ChoiceField(choices=choice_list)
    description = forms.CharField(max_length=140, required=False, widget=forms.Textarea)

class UpdateGenresForm(forms.ModelForm):

    class Meta:
        model = Musician
        widgets = {'genres': forms.CheckboxSelectMultiple}
        fields = ['genres']


class InstrumentGroupForm(forms.Form):
    choice_list = INSTRUMENT_CLASSES
    family = forms.ChoiceField(choices=choice_list)
    description = forms.CharField(max_length=50, required=False, widget=forms.Textarea)


class UpdateInstrumentsForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = ['instrument_group']
        widgets = {'instrument_group': forms.CheckboxSelectMultiple}
        labels = {'instrument_group': 'instrument family'}


class TimeFrameForm(forms.Form):
    # you need to figure out how to alter x after start_time or end_time are selected
    # I was thinking pop anything out of x that is before start time, and if end_time is
    # selected first pop anythin out of x that is after the selected end_time
    x = TIMES
    day = forms.ChoiceField(choices=DAYS)
    start_time = forms.ChoiceField(choices=x)
    end_time = forms.ChoiceField(choices=x)

class MusicianUpdateAvailabilityForm(forms.ModelForm):

    class Meta:
        model = Musician
        widgets = {'availability': forms.CheckboxSelectMultiple}
        fields = ['availability']


class UpdateFriendsForm(forms.ModelForm):

    class Meta:
        model = Musician
        fields = ['friends']
        widgets = {'friends': forms.CheckboxSelectMultiple}


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
        required = False


class NonMusicianUpdateWatchedMusicians(forms.ModelForm):

    class Meta:
        model = NonMusician
        fields = ['musicians']
        widgets = {'musicians': forms.CheckboxSelectMultiple}


class LocationTwoForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ['location']
        required = False
        labels = {'location': ''}
        widgets = {'location': MapOnlyWidget}


