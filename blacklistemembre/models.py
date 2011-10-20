from django.db import models



class BlacklisteMembre(models.Model):

    Nom = models.CharField(max_length=1000)

    Image = models.ManyToManyField('image.Image',related_name='BlacklisteMembre_Image_image_image',null=True,blank=True)

    Texte = models.CharField(max_length=1000)

    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='BlacklisteMembre_Visibilite_Visibilite_visibilite',null=True,blank=True)

    Image = models.ManyToManyField('image.Image',related_name='BlacklisteMembre_Image_image_image',null=True,blank=True)

    Lieux = models.ManyToManyField('lieux.Lieux',related_name='BlacklisteMembre_Lieux_lieux_Lieux',null=True,blank=True)

    Evenement =  models.ManyToManyField('evenement.Evenement',related_name='BlacklisteMembre_Evenement_evenement_Evenement',null=True,blank=True)

    Date = models.ManyToManyField('date.Date',related_name='BlacklisteMembre_Date_date_Date',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='BlacklisteMembre_Tag_tag_Tags',null=True,blank=True)

    Lien = models.ManyToManyField('lien.Lien',related_name='BlacklisteMembre_Lien_lien_Liens',null=True,blank=True)

    Personne = models.ManyToManyField('membre.Membre',related_name='BlacklisteMembre_Personne_membre_membre',null=True,blank=True)

    Groupe = models.ManyToManyField('groupe.Groupe',related_name='BlacklisteMembre_Groupe_groupe_groupe',null=True,blank=True)
