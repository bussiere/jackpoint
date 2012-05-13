from django import forms

class AskForm(forms.Form):
    Intitule = forms.CharField(label='Intitule',widget=forms.TextInput(attrs={'size':'512'}))
    Description = forms.CharField(label='Demande',widget=forms.Textarea)
    Tags = forms.CharField(label='Tags (doit commencer par #)',widget=forms.TextInput(attrs={'size':'512'}))
    

class AnswerForm(forms.Form):
    Reponse = forms.CharField(label='Reponse',widget=forms.Textarea)
    Tags = forms.CharField(label='Tags (doit commencer par #)',widget=forms.TextInput(attrs={'size':'512'}))
    ThreadEngineId  = forms.CharField(widget=forms.HiddenInput(),initial="0")
    QuestionId = forms.CharField(widget=forms.HiddenInput(),initial="0")
    