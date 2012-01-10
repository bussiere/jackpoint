from django.db import models











class Object(models.Model):



    Lien = models.ManyToManyField('lien.Lien',related_name='Object_Lien_lien_Liens',null=True,blank=True)



    Nom = models.CharField(max_length=10000)



    Photos = models.ManyToManyField('image.Image',related_name='Object_Photos_image_image',null=True,blank=True)



    Prix =  models.FloatField(max_length=10000)



    Membre = models.ManyToManyField('membre.Membre',related_name='Object_Membre_membre_Membre',null=True,blank=True)



    Anonymous = models.ManyToManyField('anonymous.anonymous',related_name='Object_Anonymous_anonymous_anonymous',null=True,blank=True)



    Groupe = models.ManyToManyField('groupe.Groupe',related_name='Object_Groupe_groupe_groupe',null=True,blank=True)



    Projet = models.ManyToManyField('projet.Projet',related_name='Object_Projet_projet_projet',null=True,blank=True)



    Tag = models.ManyToManyField('tag.Tag',related_name='Object_Tag_tag_tag',null=True,blank=True)



# Create your models here.




class Admin:
    pass
