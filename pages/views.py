# Create your views here.
from django.http import HttpResponse 
from django.template.loader import get_template 
from django.template import Context, Template 
from django.shortcuts import render, RequestContext 
from django.http import HttpResponse 
from pages.models import Page
from scripts_django.tools import recursif_template

def index(request):
    page = Page.objects.get(Nom="index")
    t = ""
    for template in page.Template.all() :
        t += recursif_template(template.contenu)  
    t = Template(t)
    c = RequestContext(request, dict(page=page))
    html = t.render(c)#page.Template_Page.contenu
    return HttpResponse(html)
