from django import forms
from Forum.models import MusicianResponse


class MusicianResponseForm(forms.ModelForm):

    class Meta:
        model = MusicianResponse
        fields = ['text']