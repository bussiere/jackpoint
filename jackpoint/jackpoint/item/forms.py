from django.db import models

from django import forms

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget



class ItemForm(forms.Form):
    item = forms.CharField(widget=forms.HiddenInput())
    PRIVATE_CHOICES = (('0', 'Private'), ('1', 'Public'))
    POSSEDE_CHOICES = (('0', 'Oui'), ('1', 'Non'))
    item_type = forms.CharField(widget=forms.HiddenInput(),initial="item")
    item_Possede = ChoiceField(label='Possede : ',widget=CheckboxSelectMultiple, choices=POSSEDE_CHOICES)
    item_private = ChoiceField(label='Visibility : ',widget=RadioSelect, choices=PRIVATE_CHOICES)