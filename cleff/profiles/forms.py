from __future__ import unicode_literals
from django import forms


class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Please upload a profile image')