from django.http import HttpResponse,HttpResponseRedirect
from jackpoint.invitation.forms import FirstInvitationForm,CreateInvitationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext
from jackpoint.invitation.models import Invitation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from jackpoint.skill.models import Skill
from jackpoint.carac.models import Carac
from jackpoint.item.models import Item
from django import forms
from django.forms.formsets import BaseFormSet
from jackpoint.carac.forms import CaracForm



def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = FirstInvitationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            email = form.cleaned_data['Email']
            invitation = form.cleaned_data['Invitation']
            print email
            print invitation
            try :

                invitationdb = Invitation.objects.get(Code=invitation)
                user = User.objects.create_user(email, email, invitation)
                user.InvitationAccepted = invitationdb
                user.save()
                user = authenticate(username=email, password=invitation)
                auth.login(request, user)
                return HttpResponseRedirect('../invitation/inscription/')
            except :
                invitationdb = None
            if not invitationdb :
                return HttpResponseRedirect('../') # Redirect after POST
    else:
        form = FirstInvitationForm() # An unbound form

    return render_to_response('firstinvit.html', {
        'form': form,
    },RequestContext(request))# Create your views here.
    
@login_required
def invitation_inscription(request):
    user = request.user
    if user.get_profile().Finished  == False :
        Caracs = Carac.objects.all()
        Skills = Skill.objects.all()
        Items = Item.objects.all()
        temp =  BaseFormSet
        i = 0
        for carac in Caracs :
            temp.fields[carac.Nom] = CaracForm
        Caracs = temp
        return render_to_response('invitinscription.html',{"Caracs":Caracs},RequestContext(request))
    else :
        return HttpResponseRedirect('../')
    
    
@user_passes_test(lambda u: u.has_perm('invitation.Create_Invitation'), login_url='../../')
def create_invitation(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CreateInvitationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            nombre = form.cleaned_data['NbreInvite']
            return HttpResponseRedirect('/admin/') # Redirect after POST
    else:
        form = CreateInvitationForm # An unbound form

    return render_to_response('createinvitation.html', {
        'form': form,
    })# Create your views here.

