from django import forms
from Forum.models import MusicianResponse, MusicianPost


class MusicianResponseForm(forms.ModelForm):

    class Meta:
        model = MusicianResponse
        fields = ['text']


class MusicianPostForm(forms.ModelForm):

    class Meta:
        model = MusicianPost
        fields = ['title', 'text']
