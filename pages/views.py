# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, Template
from django.shortcuts import render,RequestContext
from django.http import HttpResponse
from pages.models import Page,Categorie_Page
from moteur.models import Film
from scripts.tools import recursif_template
def Index(request):
        page = Page.objects.get(Nom="index")
	films = Film.objects.all()
	t = ""
	for template in page.Template.all() :
		t += recursif_template(template.contenu)
	print t
	
	t = Template(t)
        c = RequestContext(request, dict(page=page,films=films))
	html = t.render(c)#page.Template.contenu
	return HttpResponse(html)
