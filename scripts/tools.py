from pages.models import Template
import re
# to get include template
def recursif_template(template):
    p = re.compile('\{\%\s*include.*\%\}',re.MULTILINE)
    liste = p.findall(template)
    for l in liste :
        template_name = l.replace("{%","")
        template_name = template_name.replace("%}","")
        template_name = template_name.replace("include","")
        template_name = template_name.replace(" ","")
        try :
            template_get = Template.objects.get(Nom=template_name)
            template_get = template_get.contenu
        except Exception as e :
            print e
            print "error %s"%template_name
            template_get = ""
        template = template.replace(l,template_get)
        template = recursif_template(template)
        
    return template

##"""
##print recursif_template("""trtr
##                  {% ifequal user.id comment.user_id %} tata
##                  {% endifequal %} titi {% include template_name %} trtr
##                  {% ifequal user.id comment.user_id %} tata
##                  {% endifequal %} trtr""")
##"""
