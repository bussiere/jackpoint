from django import forms
from django.forms.widgets import PasswordInput



class MPForm(forms.Form):
    Id_Destinataire = forms.CharField(label='Id destinataire')
    Message = forms.CharField(label='Message',widget=forms.Textarea);