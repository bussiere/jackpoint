from django.db import models





class Categorie_Image(models.Model):

      Nom = models.CharField(max_length=200,null=True,blank=True)

      Note_divers = models.ManyToManyField('note.Note_divers',related_name='Categorie_Image_Note_divers_notes_Note_divers',null=True,blank=True)



class Image(models.Model):

    Nom = models.CharField(max_length=10000)

    Base64 = models.CharField(max_length=1000000)

    Membre = models.ManyToManyField('membre.Membre',related_name='Image_Membre_membre_Membre',null=True,blank=True)

    Anonymous = models.ManyToManyField('anonymous.anonymous',related_name='Image_Anonymous_anonymous_anonymous',null=True,blank=True)

    Groupe = models.ManyToManyField('groupe.Groupe',related_name='Image_Groupe_groupe_groupe',null=True,blank=True)

    Projet = models.ManyToManyField('projet.Projet',related_name='Image_Projet_projet_projet',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='Image_Tag_tag_tag',null=True,blank=True)

    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Image_Visibilite_Visibilite_visibilite',null=True,blank=True)

    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Image_Lieux_lieux_Lieux',null=True,blank=True)

    Evenement =  models.ManyToManyField('evenement.Evenement',related_name='Image_Evenement_evenement_Evenement',null=True,blank=True)

    Date = models.ManyToManyField('date.Date',related_name='Image_Date_date_Date',null=True,blank=True)

    Lien = models.ManyToManyField('lien.Lien',related_name='Image_Lien_lien_Liens',null=True,blank=True)



# Create your models here.

