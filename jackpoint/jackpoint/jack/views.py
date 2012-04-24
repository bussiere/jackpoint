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


def editJack(request):
    Caracs = Carac.objects.all()
    Skills = Skill.objects.all()
    Items = Item.objects.all()
    initial = []
    for carac in Caracs :
        initial.append({'carac': carac.Nom, 'id':carac.id})
    CaracFormSet = formset_factory(CaracForm, extra=0)
    CaracFormSet = CaracFormSet(prefix='carac', initial=initial)
    initial = []
    # algo de skills a revoir pour le classement
    for skill in Skills :
        initial.append({'skill': skill.Nom, 'id':skill.id})
    SkillFormSet = formset_factory(SkillForm, extra=0)
    SkillFormSet = SkillFormSet(prefix='skill', initial=initial)
    initial = []
    for item in Items :
        initial.append({'item': item.Nom, 'id':item.id})
    ItemFormSet = formset_factory(ItemForm, extra=0)
    ItemFormSet = ItemFormSet(prefix='item', initial=initial)
    
    print CaracFormSet.management_form
    formJack = JackRegisterForm()
    return render_to_response('invitinscription.html', {"CaracFormSet":CaracFormSet, 'SkillFormSet':SkillFormSet, 'ItemFormSet':ItemFormSet, 'formJack':formJack}, RequestContext(request))
