from django.db import models

from django import forms

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget



class ItemForm(forms.Form):
   
    PRIVATE_CHOICES = (('0', 'Private'), ('1', 'Public'))
    Possede = ChoiceField(label='Possede : ',widget=CheckboxSelectMultiple)
    private = ChoiceField(label='Visibility : ',widget=RadioSelect, choices=PRIVATE_CHOICES)