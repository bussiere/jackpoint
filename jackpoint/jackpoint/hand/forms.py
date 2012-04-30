from django.db import models

from django import forms

class AskForm(forms.Form):
    Description = forms.CharField(widget=forms.Textarea)
    Tags = forms.CharField(widget=forms.TextInput(attrs={'size':'40'}))
    