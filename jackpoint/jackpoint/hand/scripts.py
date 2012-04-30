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
from jackpoint.hand.forms import AskForm
from jackpoint.hand.models import Question
from jackpoint.jack.models import CaracUser,SkillUser,ItemUser
from jackpoint.tag.models import Tag
from jackpoint.engine.models import ThreadEngine
from jackpoint.engine.script import sendnotification
#TODO
# A factyoriser enregistrement skills carac items

def enregistrementAsk(request,caracs,skills,items,intitule,description,tags) :
    question = Question.objects.create() 
    question.save()
    question.user =  User.objects.get(id=request.user.id)
    question.Text = description
    question.Intitule = intitule
    question.save()
    #TODO
    #Factoriser et expliquer les tags
    tags = tags.split('#')
    for tag in tags :
        tag = tag.strip()
        try :
            result = Tag.objects.get(Name=tag)
        except :
            result = Tag.objects.create(Name=tag)
            result.save()
        question.Tags.add(result)
    question.save()
    for carac in caracs.keys():
        caracdb  = Carac.objects.filter(Nom=carac)
        private = False
        if caracs[carac][1] == "1" :
            private = True 
        try :
            result = CaracUser.objects.get(carac=caracdb,Level=int(caracs[carac][0]),Private=private)
        except :
            result = CaracUser.objects.create(Level=0)
            result.carac = caracdb
            result.Level = int(caracs[carac][0])
            result.Private = private
            result.save()
        question.Caracs.add(result)
    for skill in skills.keys():
        skilldb  = Skill.objects.filter(Nom=skill)
        private = False
        if skills[skill][1] == "1" :
            private = True 
        try :
            result = SkillUser.objects.get( Skills=skilldb,Level=int(skills[skill][0]),Private=private)
        except :
            result = SkillUser.objects.create(Level=0)
            result.Skills =  skilldb
            result.Private = private
            result.Level = int(skills[skill][0])
            result.save()
        question.Skills.add(result)
    for item in items.keys():
        itemdb  = Item.objects.filter(Nom=item)
        private = False
        if items[item][0] == "1" :
            private = True 
        try :
            result = ItemUser.objects.get(Item=itemdb,Private=private)
        except :
            result = ItemUser.objects.create()
            result.Item = itemdb
            result.Private = private
            result.save()
        question.Items.add(result)
    question.save()
    threadengine = ThreadEngine.objects.create()
    threadengine.Question.add(question)
    threadengine.save()
    sendnotification(question,ThreadEngine)

    