from django.contrib import admin
from lieu.models import Geohash,GPS,Rue,Adresse,Ville,CP,Pays,TypeTransport,Ligne,Region,Station,Lieu

admin.site.register(Geohash)
admin.site.register(GPS)
admin.site.register(Rue)
admin.site.register(Adresse)
admin.site.register(Ville)
admin.site.register(CP)
admin.site.register(Pays)
admin.site.register(TypeTransport)
admin.site.register(Ligne)
admin.site.register(Region)
admin.site.register(Station)
admin.site.register(Lieu)