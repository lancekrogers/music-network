from django import forms
from .models import MusMusMessage


class MusicianMessageForm(forms.ModelForm):

    class Meta:
        model = MusMusMessage
        fields = ['message']
