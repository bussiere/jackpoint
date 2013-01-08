# Create your views here.
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
from event.models import Event


@login_required
def viewid(request,id):
    event = Event.objects.get(id=id)
    return render_to_response('eventviewid.html', {'place':place},RequestContext(request))# Create

@login_required
def addevent(request):
    return render_to_response('addevent.html',RequestContext(request))
@login_required
def editevent(request):
    return render_to_response('editevent.html',RequestContext(request))