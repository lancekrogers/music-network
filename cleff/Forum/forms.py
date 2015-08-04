from django import forms
from Forum.models import MusicianResponse, MusicianPost, NonMusicianPost


class MusicianResponseForm(forms.ModelForm):

    class Meta:
        model = MusicianResponse
        fields = ['text']


class MusicianPostForm(forms.ModelForm):

    class Meta:
        model = MusicianPost
        fields = ['title', 'text']


class NonMusicianPostForm(forms.ModelForm):

    class Meta:
        model = NonMusicianPost
        fields = ['title', 'text']
