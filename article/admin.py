#coding: utf-8
from django.contrib import admin
from jackpoint.article.models import *
    
admin.site.register(Texte_Article)
admin.site.register(Article)
admin.site.register(CategorieTexte)
admin.site.register(Entete)
