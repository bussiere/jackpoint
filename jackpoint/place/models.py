from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# TODO rajouter commentaires USER sur les place

class CategoriePlace(models.Model):
    Nom = models.CharField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)

class Url(models.Model):
    Link = models.TextField(max_length=1024, null=True, blank=True)
    Description = models.TextField(max_length=1024, null=True, blank=True) 
    def __unicode__(self):
        return str(self.Link)

class Place(models.Model):
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    Categorie = models.ManyToManyField('CategoriePlace', null=True, blank=True)
    Texte = models.TextField(max_length=1024, null=True, blank=True)
    Url = models.ManyToManyField('Url', null=True, blank=True)
    Skills = models.ManyToManyField("jack.SkillUser", null=True, blank=True)
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Items = models.ManyToManyField("jack.ItemUser", null=True, blank=True)
    Caracs = models.ManyToManyField("jack.CaracUser", null=True, blank=True)
    Horaire = models.ManyToManyField('date.DateJourHoraire',null=True, blank=True)
    Lieu = models.ForeignKey('lieu.Lieu',null=True, blank=True)
    Createur =  models.ForeignKey(User, unique=False, null=True, blank=True)  
    
    #TODO
    # Why not faire le save et ecrire le texte en fonciton de la langue ?
    def __unicode__(self):
        return str(self.Nom)
NoteAvis = (
    (0, 'Aucun avis'),
    (1, 'Beurk'),
    (2, 'bof'),
    (3, 'Pas mal'),
    (4, 'Bien'),
    (5, 'Tres bien'),
)

class Avis(models.Model):
    Createur =  models.ForeignKey(User, unique=False, null=True, blank=True) 
    Texte = models.TextField(max_length=2048, null=True, blank=True)
    Note =   models.IntegerField(choices=NoteAvis)
    
# Create your models here.
