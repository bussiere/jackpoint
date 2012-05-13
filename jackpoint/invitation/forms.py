from django.db import models

from django import forms

class FirstInvitationForm(forms.Form):
    Email = forms.EmailField(max_length=100)
    Invitation = forms.CharField(max_length=100)
    
class CreateInvitationForm(forms.Form):
    NbreInvite = forms.IntegerField()
