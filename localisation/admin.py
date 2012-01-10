#coding: utf-8
from django.contrib import admin
from jackpoint.localisation.models import *
    
admin.site.register(Etat)
admin.site.register(Ville)
admin.site.register(Pays)
admin.site.register(Adresse)
admin.site.register(Localisation)
admin.site.register(Region)
admin.site.register(NomsEndroit)
