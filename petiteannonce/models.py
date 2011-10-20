from django.db import models



class Categorie_PetiteAnnonce(models.Model):

    Nom = models.CharField(max_length=10000)

   

class PrixTotal(models.Model):

    Prix =  models.FloatField(max_length=1000000)



class PrixIndividuel(models.Model):

    Prix =  models.FloatField(max_length=1000000)



class Prix(models.Model):

    Prix =  models.FloatField(max_length=1000000)



class FdpIndividuel(models.Model):

    Prix =  models.FloatField(max_length=1000000)



class Fdp(models.Model):

    Prix =  models.FloatField(max_length=1000000)  

    

class Annonce(models.Model):

    Categorie_PetiteAnnonce = models.ManyToManyField(Categorie_PetiteAnnonce,null=True,blank=True)

    Nom = models.CharField(max_length=10000)

    Photos = models.ManyToManyField('image.Image',related_name='petiteanonce_Photos_image_image',null=True,blank=True)

    Prix = models.ManyToManyField(Prix,null=True,blank=True)

    PrixTotal = models.ManyToManyField(PrixTotal,null=True,blank=True)

    PrixIndividuel = models.ManyToManyField(PrixIndividuel,null=True,blank=True)

    FdpIndividuel = models.ManyToManyField(FdpIndividuel,null=True,blank=True)

    Fdp = models.ManyToManyField(Fdp,null=True,blank=True)

    Membre = models.ManyToManyField('membre.Membre',related_name='petiteanonce_Membre_membre_Membre',null=True,blank=True)

    Anonymous = models.ManyToManyField('anonymous.anonymous',related_name='petiteanonce_Anonymous_anonymous_anonymous',null=True,blank=True)

    Groupe = models.ManyToManyField('groupe.Groupe',related_name='petiteanonce_Groupe_groupe_groupe',null=True,blank=True)

    Projet = models.ManyToManyField('projet.Projet',related_name='petiteanonce_Projet_projet_projet',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='petiteanonce_Tag_tag_tag',null=True,blank=True)

    Lien = models.ManyToManyField('lien.Lien',related_name='petiteanonce_Lien_lien_Liens',null=True,blank=True)

