from django.db import models

from django import forms

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple,PasswordInput
from django.forms.extras.widgets import SelectDateWidget



class JackRegisterForm(forms.Form):
    jack_username = forms.CharField(label='Pseudo : ')
    jack_email = forms.EmailField(label='Email : ')
    jack_password1 = forms.CharField(label='Password : ',widget=PasswordInput)
    jack_password2 = forms.CharField(label='Password Confirmation : ',widget=PasswordInput)
    jack_Avatar = forms.ImageField(label='Avatar :')
    jack_Bio = forms.CharField(label='Bio :',widget=forms.Textarea);