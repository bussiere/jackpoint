
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.db.models.loading import cache as model_cache
if not model_cache.loaded:
    model_cache.get_models()
from pages.models import Page, Template
import settings

t1 = Template(Nom="template_index",contenu="""bienvenue<br>
<a href="../logout/">logout</a>""")
t1.save()
p = Page(Nom="index",Template=t1)
p.save()

t2 = Template(Nom="template_indexvide",contenu="""   <form method="post" action=".">{% csrf_token %}
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="login" />
    </form>""")
t2.save()
p = Page(Nom="indexvide",Template=t2)
p.save()