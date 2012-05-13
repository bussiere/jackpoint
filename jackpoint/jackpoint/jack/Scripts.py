# Create your views here.
from django.http import HttpResponseRedirect
from invitation.forms import FirstInvitationForm,CreateInvitationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from invitation.models import Invitation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from skill.models import Skill
from carac.models import Carac
from item.models import Item
from carac.forms import CaracForm
from skill.forms import SkillForm
from item.forms import ItemForm
from jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet
from jack.models import CaracUser,SkillUser,ItemUser
from carac.models import Carac
from skill.models import Skill
from invitation.script import classer_invitation

@login_required
def enregistrementJack(request,jack,caracs,skills,items,invitation=None):
    retour = True
    u = User.objects.get(id=request.user.id)
#    jack["jack_username"]=jack_username
#    jack["jack_email"] = jack_email
#    jack["jack_password1"]= jack_password1
#    jack["jack_password2"]=jack_password2
#    jack["jack_Bio"]=jack_Bio
    u.get_profile().Pseudo = jack["jack_username"]
    u.get_profile().Email = jack["jack_email"]
    u.get_profile().Bio = jack["jack_Bio"]
    u.save()
    u.get_profile().save()
    u.get_profile().Caracs.clear()
    u.get_profile().Skills.clear()
    u.get_profile().Items.clear()
    #TODO
    #crade a revoir
    for carac in caracs.keys():
        caracdb  = Carac.objects.get(Nom=carac)
        private = False
        if caracs[carac][1] == "1" :
            private = True 
        try :
            result = CaracUser.objects.get(carac=caracdb,Level=int(caracs[carac][0]),Private=private)
        except :
            result = CaracUser.objects.create(Level=0)
            result.Carac.add(caracdb)
            result.Level = int(caracs[carac][0])
            result.Private = private
            result.save()
        u.get_profile().Caracs.add(result)
    for skill in skills.keys():
        skilldb  = Skill.objects.get(Nom=skill)
        private = False
        if skills[skill][1] == "1" :
            private = True 
        try :
            result = SkillUser.objects.get( Skills=skilldb,Level=int(skills[skill][0]),Private=private)
        except :
            result = SkillUser.objects.create(Level=0)
            result.Skill.add(skilldb)
            result.Private = private
            result.Level = int(skills[skill][0])
            result.save()
        u.get_profile().Skills.add(result)
    for item in items.keys():
        itemdb  = Item.objects.get(Nom=item)
        private = False
        if items[item][0] == "1" :
            private = True 
        try :
            result = ItemUser.objects.get(Item=itemdb,Private=private)
        except :
            result = ItemUser.objects.create()
            result.Item.add(itemdb)
            result.Private = private
            result.save()
        u.get_profile().Items.add(result)
    u.get_profile().save()
    u.save()
    #faire la verif des mdps
    if (jack["jack_password1"]==jack["jack_password2"] and jack["jack_password1"] != ""):
        u.set_password(jack["jack_password1"])
        u.get_profile().Finished = True;
        classer_invitation(u.get_profile().InvitationAccepted)            
    else :
        retour = False
    u.save()
    # faire la verif pour l'invitation et la passer a used.
        
    
    return retour