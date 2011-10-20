# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def Presentation(request):
	t = get_template('index.html')
	now = "titi"
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)
