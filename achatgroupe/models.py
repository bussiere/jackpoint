from django.db import models





class Categorie_AchatGroupe(models.Model):

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

    Categorie_AchatGroupe = models.ManyToManyField(Categorie_AchatGroupe,null=True,blank=True)

    Nom = models.CharField(max_length=10000)

    Photos = models.ManyToManyField('image.Image',related_name='Photo_annonce',null=True,blank=True)

    Prix = models.ManyToManyField(Prix,null=True,blank=True)

    PrixTotal = models.ManyToManyField(PrixTotal,null=True,blank=True)

    PrixIndividuel = models.ManyToManyField(PrixIndividuel,null=True,blank=True)

    FdpIndividuel = models.ManyToManyField(FdpIndividuel,null=True,blank=True)

    Fdp = models.ManyToManyField(Fdp,null=True,blank=True)

    Membre = models.ManyToManyField('membre.Membre',related_name='Proprietaires_annonce',null=True,blank=True)

    Anonymous = models.ManyToManyField('anonymous.Anonymous',related_name='Anonyme_annonce',null=True,blank=True)

    Groupe = models.ManyToManyField('groupe.Groupe',related_name='Groupes_annonce',null=True,blank=True)

    Projet = models.ManyToManyField('projet.Projet',related_name='Projets_annonce',null=True,blank=True)

    Tag = models.ManyToManyField('tag.Tag',related_name='Tags_annonce',null=True,blank=True)

    Lien = models.ManyToManyField('lien.Lien',related_name='Liens_annonce',null=True,blank=True)
