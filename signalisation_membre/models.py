from django.db import models



# Create your models here.

class signalisation_membre(models.Model):

	Reference = models.CharField(max_length=10000)

	Texte = models.CharField(max_length=10000)

	Membre = models.ManyToManyField('membre.Membre',null=True,blank=True)
