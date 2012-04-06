from django.http import HttpResponse,HttpResponseRedirect
from jackpoint.engine.forms import LoginForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            return HttpResponseRedirect('/X/') # Redirect after POST
    else:
        form = LoginForm() # An unbound form

    return render_to_response('index.html', {
        'form': form
    },RequestContext(request))

