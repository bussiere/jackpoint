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
from jackpoint.engine.models import Notification
from jackpoint.carac.forms import CaracForm
from jackpoint.skill.forms import SkillForm
from jackpoint.item.forms import ItemForm
from jackpoint.jack.forms import JackRegisterForm
from django.forms.formsets import formset_factory
from django.forms.formsets import BaseFormSet





@login_required
def index(request):
    u = User.objects.get(id=request.user.id)
    notifications = Notification.objects.filter(User=u)
    return render_to_response('x.html', {'notifications':notifications
    },RequestContext(request))
