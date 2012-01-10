from django.db import models











# Create your models here.



class Avis(models.Model):



	Texte = models.CharField(max_length=10000)



	Membre = models.ManyToManyField('membre.Membre',null=True,blank=True)



	Publiable = models.NullBooleanField(blank=True)



	Lien = models.ManyToManyField('lien.Lien',null=True,blank=True)



	Note_divers = models.ManyToManyField('note.Note_divers',related_name='Lieux_Avis_Note_divers_notes_Note_divers',null=True,blank=True)



	Geohash = models.CharField(max_length=1000)



	Tags = models.ManyToManyField('tag.Tag',related_name='Lieux_Avis_Tags',null=True,blank=True)







class TypeLieux(models.Model):



	Nom = models.CharField(max_length=10000)



	Tags = models.ManyToManyField('tag.Tag',related_name='TypeLieux_Tags',null=True,blank=True)







class Lieux(models.Model):



	Localisation = models.ManyToManyField('localisation.Localisation',related_name='Lieux_Localisation_localisation_localisation',null=True,blank=True)



	Texte = models.CharField(max_length=10000)



	Notation = models.ManyToManyField('notation.Notation',related_name='Lieux_Notation_Notation_notation',null=True,blank=True)



	Liens = models.ManyToManyField('lien.Lien',related_name='Lieux_Liens_liens_Lien',null=True,blank=True)



	Horaire = models.ManyToManyField('horaire.Horaire',related_name='Lieux_Horaire',null=True,blank=True)



	Tags = models.ManyToManyField('tag.Tag',related_name='Lieux_Tags',null=True,blank=True)



	Note =  models.ManyToManyField('note.Note_divers',related_name='Lieux_Note_notes_Note_divers',null=True,blank=True)




class Admin:
    pass
