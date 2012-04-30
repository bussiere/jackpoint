from django import forms

class AskForm(forms.Form):
    Intitule = forms.CharField(label='Intitule',widget=forms.TextInput(attrs={'size':'512'}))
    Description = forms.CharField(label='Demande',widget=forms.Textarea)
    Tags = forms.CharField(label='Tags (doit commencer par #)',widget=forms.TextInput(attrs={'size':'512'}))
    

class AnswerForm(forms.Form):
    Description = forms.CharField(label='Reponse',widget=forms.Textarea)
    Tags = forms.CharField(label='Tags (doit commencer par #)',widget=forms.TextInput(attrs={'size':'512'}))
    ThreadEngineId = carac_type = forms.CharField(widget=forms.HiddenInput(),initial="0")
    