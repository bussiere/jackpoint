from django.http import HttpResponse,HttpResponseRedirect
from jackpoint.engine.forms import LoginForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from jackpoint.invitation.forms import FirstInvitationForm,CreateInvitationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from jackpoint.invitation.models import Invitation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from jackpoint.skill.models import Skill
from jackpoint.carac.models import Carac
from jackpoint.item.models import Item
from jackpoint.carac.forms import CaracFormChoice
from jackpoint.skill.forms import SkillForm
from jackpoint.item.forms import ItemForm
from jackpoint.jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from jackpoint.hand.scripts import enregistrementAsk
from jackpoint.hand.forms import AskForm
@login_required
def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AskForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            return HttpResponseRedirect('/X/') # Redirect after POST
    else:
        form = AskForm() # An unbound form

    return render_to_response('questions.html', {
        'form': form
    },RequestContext(request))# Create


@login_required
def ask(request):
    if request.method == 'POST': # If the form has been submitted...
        form = AskForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            #TODO
            # a factoriser
            nbre_carac = int(request.POST['carac-TOTAL_FORMS'])
            nbre_initial_carac = request.POST['carac-INITIAL_FORMS']
            levelcarac="carac-#-carac_level"
            namecarac = "carac-#-carac"
            privatecarac = "carac-#-carac_private"
            compteur_carac = 0
            caracs = {}
            while compteur_carac < nbre_carac :
                caracs[request.POST["carac-%d-carac"%compteur_carac]] = [request.POST["carac-%d-carac_level"%compteur_carac],request.POST["carac-%d-carac_private"%compteur_carac]]
                compteur_carac += 1
            nbr_skills = int(request.POST['skill-TOTAL_FORMS'])
            nbr_initial_skills = request.POST['skill-INITIAL_FORMS']
            levelskill = "skill-#-skill_level"
            nameskill = "skill-#-skill"
            privateskill = "skill-#-skill_private"
            compteur_skill = 0
            skills = {}
            while compteur_skill < nbr_skills :
                if int(request.POST["skill-%d-skill_level"%compteur_skill]) > 0 :
                    skills[request.POST["skill-%d-skill"%compteur_skill]] = [request.POST["skill-%d-skill_level"%compteur_skill],request.POST["skill-%d-skill_private"%compteur_skill]]
                compteur_skill += 1
            nbre_item = int(request.POST['item-TOTAL_FORMS'])
            nbre_initial_item = request.POST['item-INITIAL_FORMS']
            Possede = "item-#-item_Possede"
            nameitem = "item-#-item"
            privatecarac = "item-#-item_private"
            compteur_item = 0
            items = {}
            while compteur_item < nbre_item :
                if int(request.POST["item-%d-item_Possede"%compteur_item]) > 0 :
                    items[request.POST['item-%d-item'%compteur_item]] = request.POST["item-%d-item_private"%compteur_item]
                compteur_item += 1
            print caracs
            print skills
            print items
            retour = enregistrementAsk(request,caracs,skills,items)  
            return HttpResponseRedirect('../../hand/view/') # Redirect after POST
    else:
        form = AskForm() # An unbound form
        Caracs = Carac.objects.all()
        Skills = Skill.objects.all()
        Items = Item.objects.all()
        initial = []
        for carac in Caracs :
            initial.append({'carac': carac.Nom,'id':carac.id})
        CaracFormSet = formset_factory(CaracFormChoice, extra=0)
        CaracFormSet = CaracFormSet(prefix='carac',initial=initial)
        initial = []
        # algo de skills a revoir pour le classement
        for skill in Skills :
            initial.append({'skill': skill.Nom,'id':skill.id})
        SkillFormSet = formset_factory(SkillForm, extra=0)
        SkillFormSet = SkillFormSet(prefix='skill',initial=initial)
        initial = []
        for item in Items :
            initial.append({'item': item.Nom,'id':item.id})
        ItemFormSet = formset_factory(ItemForm, extra=0)
        ItemFormSet = ItemFormSet(prefix='item',initial=initial)


    return render_to_response('ask.html', {
        'form': form,"CaracFormSet":CaracFormSet,'SkillFormSet':SkillFormSet,'ItemFormSet':ItemFormSet
    },RequestContext(request))# Create your views here.
    



