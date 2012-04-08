from django.db import models

from django import forms

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget



class CaracForm(forms.Form):
    carac = forms.CharField(widget=forms.HiddenInput())
    id = forms.CharField(widget=forms.HiddenInput())
    type = forms.CharField(widget=forms.HiddenInput(),default="carac")
    CARAC_CHOICES = (('1', 'Nul'), ('2', 'Bof'),('3', 'Moyen'),('4', 'Bon'),('5', 'Excellent'))
    PRIVATE_CHOICES = (('0', 'Private'), ('1', 'Public'))
    level = ChoiceField(label='Niveau : ',widget=RadioSelect, choices=CARAC_CHOICES)
    private = ChoiceField(label='Visibility : ',widget=RadioSelect, choices=PRIVATE_CHOICES)