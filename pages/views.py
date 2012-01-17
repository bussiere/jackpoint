# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, Template 
from django.shortcuts import render, RequestContext 
from django.http import HttpResponse 
from pages.models import Page
from scripts_django.tools import recursif_template

def index(request,logouts=""):
    output = ""
    output += logouts
    if (logouts == 'logout'):
            logout(request)

    try :
        if (request.POST['username'] or request.POST['password']):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    login(request, user)
                    output =  Page.objects.get(Nom="index")
                    # Redirect to a success page.
                else:
                    pass
            else:
                output = Page.objects.get(Nom="indexvide")
        else :
            output = Page.objects.get(Nom="indexvide")
    except :
        if request.user.is_authenticated():
            output = Page.objects.get(Nom="index")
        else :
            output = Page.objects.get(Nom="indexvide")
    t = ""
    for template in output.Template.all() :
        t += recursif_template(template.contenu)  
    t = Template(t)
    c = RequestContext(request)
    return HttpResponse(t.render(c))# Create your views here.
