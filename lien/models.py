from django.db import models



# Create your models here.



class CategorieLien(models.Model):

    Nom = models.CharField(max_length=200,null=True,blank=True)

    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Categorie_Lien_Note_divers_notes_Note_divers',null=True,blank=True)

    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Categorie_Lien_Visibilite_Visibilite',null=True,blank=True)

class Lien(models.Model):

    Categorie = models.ManyToManyField(CategorieLien,null=True,blank=True)

    Nom = models.CharField(max_length=200,null=True,blank=True)

    url = models.CharField(max_length=500,null=True,blank=True)

    alt = models.CharField(max_length=400,null=True,blank=True)

    Texte_contenu = models.ManyToManyField('presentation.Texte_contenu',related_name='Lien_Texte_contenu_presentation_Texte_contenu',null=True,blank=True)

    MiseEnForme = models.ManyToManyField('presentation.MiseEnForme',related_name='Lien_MiseEnForme_presentation_MiseEnForme',null=True,blank=True)

    Note_divers = models.ManyToManyField('note.Note_divers',related_name='Lien_Note_divers_notes_Note_divers',null=True,blank=True)

    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Lien_Visibilite_Visibilite',null=True,blank=True)





class LienFacebook(models.Model):

    LienFacaebook = models.ManyToManyField(Lien,null=True,blank=True)



class LienTwitter(models.Model):

    LienTwitter = models.ManyToManyField(Lien,null=True,blank=True)

