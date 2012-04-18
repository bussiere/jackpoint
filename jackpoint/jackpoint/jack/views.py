# Create your views here.
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
from jackpoint.carac.forms import CaracForm
from jackpoint.skill.forms import SkillForm
from jackpoint.item.forms import ItemForm
from jackpoint.jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from jackpoint.jack.models import CaracUser,SkillUser,ItemUser
from jackpoint.carac.models import Carac
from jackpoint.skill.models import Skill

@login_required
def enregistrementJack(request,jack,caracs,skills,items):
    retour = True
    u = User.objects.get(request.user)
#    jack["jack_username"]=jack_username
#    jack["jack_email"] = jack_email
#    jack["jack_password1"]= jack_password1
#    jack["jack_password2"]=jack_password2
#    jack["jack_Bio"]=jack_Bio
    u.Pseudo = jack["jack_username"]
    u.email = jack["jack_email"]
    u.Bio = jack["jack_Bio"]
    u.Caracs.clear()
    u.Skills.clear()
    u.Items.clear()
    #TODO
    #crade a revoir
    for carac in caracs.keys():
        caracdb  = Carac.objects.filter(Nom=carac)
        private = False
        if caracs[carac][1] == "1" :
            private = True 
        result = CaracUser.objects.filter(carac=caracdb,Level=int(caracs[carac][0]),Private=private)
        if result == None :
            result = CaracUser.objects.create(carac=caracdb,Level=int(caracs[carac][0]),Private=private)
        u.Caracs.add(result)
    for skill in skills.keys():
        skilldb  = Skill.objects.filter(Nom=skill)
        private = False
        if skills[skill][1] == "1" :
            private = True 
        result = SkillUser.objects.filter( Skills=skilldb,Level=int(skills[skill][0]),Private=private)
        if result == None :
            result = SkillUser.objects.create( Skills=skilldb,Level=int(skills[skill][0]),Private=private)
        u.Skills.add(result)
    for item in items.keys():
        itemdb  = Item.objects.filter(Nom=item)
        private = False
        if items[item][0] == "1" :
            private = True 
        result = ItemUser.objects.filter(Item=itemdb,Private=private)
        if result == None :
            result = ItemUser.objects.create(Item=itemdb,Private=private)
        u.Items.add(result)
    u.save()
    #faire la verif des mdps
    if (jack["jack_password1"]==jack["jack_password2"] and jack["jack_password1"] != ""):
        u.set_password(jack["jack_password1"])               
    else :
        retour = False
    u.save()
    # faire la verif pour l'invitation et la passer a used.
        
    
    return retour