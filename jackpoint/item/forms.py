from django.db import models

from django import forms

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget



class ItemForm(forms.Form):
    item = forms.CharField(widget=forms.HiddenInput())
    PRIVATE_CHOICES = (('0', 'Private'), ('1', 'Public'))
    POSSEDE_CHOICES = (('0', 'Non'), ('1', 'Oui'))
    item_type = forms.CharField(widget=forms.HiddenInput(),initial="item")
    item_Possede = ChoiceField(label='Possede : ',widget=RadioSelect, choices=POSSEDE_CHOICES,initial=0)
    item_private = ChoiceField(label='Visibility : ',widget=RadioSelect, choices=PRIVATE_CHOICES,initial=1)
    

class ItemFormChoice(forms.Form):
    item = forms.CharField(widget=forms.HiddenInput())
    POSSEDE_CHOICES = (('0', 'Non'), ('1', 'Oui'))
    item_type = forms.CharField(widget=forms.HiddenInput(),initial="item")
    item_Possede = ChoiceField(label='Possede : ',widget=RadioSelect, choices=POSSEDE_CHOICES,initial=0)
