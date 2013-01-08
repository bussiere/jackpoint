from django.db import models

from django import forms

from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

#TODO
# a nettoyer le caracchoice contre un skill choice 

class SkillForm(forms.Form):
    skill = forms.CharField(widget=forms.HiddenInput())
    skill_id = forms.CharField(widget=forms.HiddenInput())
    skill_parent = forms.CharField(widget=forms.HiddenInput())
    skill_child = forms.CharField(widget=forms.HiddenInput())
    skill_niveau = forms.CharField(widget=forms.HiddenInput())
    skill_type = forms.CharField(widget=forms.HiddenInput(),initial="skill")
    CARAC_CHOICES = (('0', 'Ne la possede pas'),('1', 'Nul'), ('2', 'Bof'),('3', 'Moyen'),('4', 'Bon'),('5', 'Excellent'))
    PRIVATE_CHOICES = (('0', 'Private'), ('1', 'Public'))
    skill_level = ChoiceField(label='Niveau : ',widget=RadioSelect, choices=CARAC_CHOICES,initial=0)
    skill_private = ChoiceField(label='Visibility : ',widget=RadioSelect, choices=PRIVATE_CHOICES,initial=1)
    
    
class SkillFormChoice(forms.Form):
    skill = forms.CharField(widget=forms.HiddenInput())
    skill_id = forms.CharField(widget=forms.HiddenInput())
    skill_parent = forms.CharField(widget=forms.HiddenInput())
    skill_child = forms.CharField(widget=forms.HiddenInput())
    skill_niveau = forms.CharField(widget=forms.HiddenInput())
    skill_type = forms.CharField(widget=forms.HiddenInput(),initial="skill")
    CARAC_CHOICES = (('-1', 'Aucun'),('0', 'Peu importe'),('1', 'Nul'), ('2', 'Bof'),('3', 'Moyen'),('4', 'Bon'),('5', 'Excellent'))
    skill_level = ChoiceField(label='Niveau : ',widget=RadioSelect, choices=CARAC_CHOICES,initial=-1)
