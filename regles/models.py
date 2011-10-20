from django.db import models



# Create your models here.





class Ratio(models.Model):

    Ratio = models.FloatField()

    Nom = models.CharField(max_length=200)

    Note_divers = models.ManyToManyField('note.Note_divers')



#a revoir et a augmenter

class Regle(models.Model):

    Type = models.CharField(max_length=200)

    Membre = models.ManyToManyField('membre.Membre')

    TagVendeurs = models.ManyToManyField('tag.Tag',related_name="Tags Vendeurs")

    TagMoins = models.ManyToManyField('tag.Tag',related_name="Tags Moins Vendeurs")

    TagPref = models.ManyToManyField('tag.Tag',related_name="Tags Les Preferes")

    FamilleTagVendeurs = models.ManyToManyField('tag.FamilleTag',related_name="Famille vendeurs")

    FamilleTagMoins = models.ManyToManyField('tag.FamilleTag',related_name="Famille moins vendeur")

    FamilleTagPref = models.ManyToManyField('tag.FamilleTag',related_name="famille Pref")

    Ratio = models.ManyToManyField('regles.Ratio')

    Note_divers = models.ManyToManyField('note.Note_divers')

