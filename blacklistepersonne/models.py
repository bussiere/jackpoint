from django.db import models



# Create your models here.

class BlacklisteMembre(models.Model):

    Nom = models.CharField(max_length=1000)

    Image = models.ManyToManyField('image.Image',related_name='BlacklistePersonne_Image_image_image',null=True,blank=True)

    Texte = models.CharField(max_length=1000)

    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='BlacklistePersonne_Visibilite_Visibilite_visibilite',null=True,blank=True)

    Image = models.ManyToManyField('image.Image',related_name='BlacklistePersonne_Image_image_image',null=True,blank=True)

    Lieux = models.ManyToManyField('lieux.Lieux',related_name='BlacklistePersonne_Lieux_lieux_Lieux',null=True,blank=True)

    Evenement =  models.ManyToManyField('evenement.Evenement',related_name='BlacklistePersonne_Evenement_evenement_Evenement',null=True,blank=True)

    Date = models.ManyToManyField('date.Date',related_name='BlacklistePersonne_Date_date_Date',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='BlacklistePersonne_Tag_tag_Tags',null=True,blank=True)

    Lien = models.ManyToManyField('lien.Lien',related_name='BlacklistePersonne_Lien_lien_Liens',null=True,blank=True)

    Personne = models.ManyToManyField('personne.Personne',related_name='BlacklistePersonne_Personne_personne_Personne',null=True,blank=True)

    Groupe = models.ManyToManyField('personnegroupe.PersonneGroupe',related_name='BlacklistePersonne_Groupe_personnegroupe_personnegroupe',null=True,blank=True)
