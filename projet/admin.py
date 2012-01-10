#coding: utf-8
from django.contrib import admin
from jackpoint.projet.models import *
    
admin.site.register(Projet)
admin.site.register(ProjetAmis)
admin.site.register(Date_Visite)
