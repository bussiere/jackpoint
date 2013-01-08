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
from jack.scripts import enregistrementJack
    
    
def index(request):
    pass
    
    
@login_required
def invitation_inscription(request):
    pass
 
@login_required
def validation_inscription(request):
    pass

        
        
    
@user_passes_test(lambda u: u.has_perm('invitation.Create_Invitation'), login_url='../../')
def create_invitation(request):
    pass
