from django.db import models







# Create your models here.







class Categorie_Note(models.Model):



    Nom = models.CharField(max_length=400)







class Note_divers(models.Model):



    Nom = models.CharField(max_length=400)

    Texte = models.CharField(max_length=10000)

    Membre = models.ManyToManyField('membre.Membre', null=True, blank=True)

    Visibilite = models.ManyToManyField('visibilite.Visibilite', null=True, blank=True)

    Lien = models.ManyToManyField('lien.Lien', null=True, blank=True)

    Geohash = models.CharField(max_length=1000)

    Tags = models.ManyToManyField('tag.Tag')

    Categorie = models.ManyToManyField(Categorie_Note)




class Admin:
    pass
