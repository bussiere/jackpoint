from django.db import models



# Create your models here.

class Tag(models.Model):

    Nom = models.CharField(max_length=200)

    Creation = models.DateTimeField('date published')



class FamilleTag(models.Model):

    Nom = models.CharField(max_length=200)

    Tag = models.ManyToManyField(Tag)



class Asso_Tag(models.Model):

	Tag = models.ManyToManyField(Tag)

	FamilleTag= models.ManyToManyField(FamilleTag)

	Membre = models.ManyToManyField('membre.Membre')

