# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from skill.models import Skill
from carac.models import Carac
from item.models import Item
from jack.models import UserProfile
from carac.forms import CaracForm
from skill.forms import SkillForm
from item.forms import ItemForm
from jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.contrib.auth.models import User
from jack.scripts import enregistrementJack
from django.http import HttpResponseRedirect
from jack.models import CaracUser,SkillUser,ItemUser
from place.models import Place

@login_required
def viewid(request,id):
    place = Place.objects.get(id=id)
    return render_to_response('placeviewid.html', {'place':place},RequestContext(request))# Create

@login_required
def addplace(request):
    return render_to_response('addplace.html',RequestContext(request))