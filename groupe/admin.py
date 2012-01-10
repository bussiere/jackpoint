#coding: utf-8
from django.contrib import admin
from jackpoint.groupe.models import *
    
admin.site.register(Groupe)
admin.site.register(GroupeAmis)
admin.site.register(Date_Visite)
