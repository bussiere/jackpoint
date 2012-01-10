#coding: utf-8
from django.contrib import admin
from jackpoint.achatgroupe.models import *
    
admin.site.register(Annonce)
admin.site.register(Prix)
admin.site.register(PrixIndividuel)
admin.site.register(Categorie_AchatGroupe)
admin.site.register(Fdp)
admin.site.register(FdpIndividuel)
admin.site.register(PrixTotal)
