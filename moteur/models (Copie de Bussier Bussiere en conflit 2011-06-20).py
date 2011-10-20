from django.db import models

# Create your models here.

class Texte(models.Model):
    Description = models.CharField(max_length=800)
    Texte = models.CharField(max_length=10000)
    Langue = models.ManyToManyField(Langue)
    Categorie = models.ManyToManyField(Categorie_Texte)
    Note_divers = models.ManyToManyField('note.Note_divers')

class NiveauCategorie(models.Model):
    Niveau = models.CharField(max_length=10000)

class NiveauPost(models.Model):
    Niveau = models.CharField(max_length=10000)


class NiveauReponse(models.Model):
    Niveau = models.CharField(max_length=10000)


class Post(models.Model):
    Lien = models.ManyToManyField('Notation',null=True,blank=True)
    Membre = models.ManyToManyField('membre.Membre')
    Texte = models.ManyToManyField('Texte',null=True,blank=True)
    NiveauPost = models.ManyToManyField('NiveauPost',null=True,blank=True)
    NiveauReponse = models.ManyToManyField('NiveauPost',null=True,blank=True)


class Reponse(models.Model):
    Post = models.ManyToManyField('Post',null=True,blank=True)
    Lien = models.ManyToManyField('Notation',null=True,blank=True)
    Membre = models.ManyToManyField('membre.Membre')
    Texte = models.ManyToManyField('Texte',null=True,blank=True)
    