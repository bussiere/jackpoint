#coding: utf-8
from django.contrib import admin
from jackpoint.petiteannonce.models import *
    
admin.site.register(Annonce)
admin.site.register(Prix)
admin.site.register(PrixIndividuel)
admin.site.register(FdpIndividuel)
admin.site.register(Fdp)
admin.site.register(Categorie_PetiteAnnonce)
admin.site.register(PrixTotal)
