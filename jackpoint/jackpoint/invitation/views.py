from django.http import HttpResponse,HttpResponseRedirect
from jackpoint.invitation.forms import FirstInvitationForm,CreateInvitationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.template import RequestContext

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = FirstInvitationForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            email = form.cleaned_data['Email']
            invitation = form.cleaned_data['invitation']
            print email
            print invitation
            return HttpResponseRedirect('/X/') # Redirect after POST
    else:
        form = FirstInvitationForm() # An unbound form

    return render_to_response('firstinvit.html', {
        'form': form,
    },RequestContext(request))# Create your views here.
    
    
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

