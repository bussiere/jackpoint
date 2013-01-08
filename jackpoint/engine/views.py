from django.http import HttpResponseRedirect
from engine.forms import LoginForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login


def index(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            username = form.cleaned_data['Username']
            password = form.cleaned_data['pw']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/X/') # Redirect after POST
    else:
        form = LoginForm() # An unbound form

    return render_to_response('index.html', {
        'form': form
    },RequestContext(request))

