#coding: utf-8
from django.contrib import admin
from jackpoint.lien.models import *
    
admin.site.register(Lien)
admin.site.register(CategorieLien)
admin.site.register(LienFacebook)
admin.site.register(LienTwitter)
