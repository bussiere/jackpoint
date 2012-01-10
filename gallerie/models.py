from django.db import models











class Gallerie(models.Model):



    Nom = models.CharField(max_length=1000)



    Image = models.ManyToManyField('image.Image',related_name='Gallerie_Image_image_image',null=True,blank=True)



    CategorieGallerie = models.CharField(max_length=1000)



    Texte = models.CharField(max_length=1000)



    Visibilite = models.ManyToManyField('visibilite.Visibilite',related_name='Gallerie_Visibilite_Visibilite_visibilite',null=True,blank=True)



    Image = models.ManyToManyField('image.Image',related_name='Gallerie_Image_image_image',null=True,blank=True)



    Lieux = models.ManyToManyField('lieux.Lieux',related_name='Gallerie_Lieux_lieux_Lieux',null=True,blank=True)



    Evenement =  models.ManyToManyField('evenement.Evenement',related_name='Gallerie_Evenement_evenement_Evenement',null=True,blank=True)



    Date = models.ManyToManyField('date.Date',related_name='Gallerie_Date_date_Date',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Gallerie_Tag_tag_Tags',null=True,blank=True)



    Lien = models.ManyToManyField('lien.Lien',related_name='Gallerie_Lien_lien_Liens',null=True,blank=True)



# Create your models here.




class Admin:
    pass
