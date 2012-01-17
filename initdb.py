
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()
from pages.models import Page, Template
import settings

t = Template(Nom="template_index",contenu="""bienvenue<br>
<a href="../logout/">logout</a>""")
t.save()
p = Page(Nom="index",Template=Template.objects.get("template_index"))
p.save()

t = Template(Nom="template_indexvide",contenu="""   <form method="post" action=".">{% csrf_token %}
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="login" />
    </form>""")
t.save()
p = Page(Nom="indexvide",Template=Template.objects.get("template_indexvide"))
p.save()