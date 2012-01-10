from django.db import models







# Create your models here.







class NomsEndroit(models.Model):



	Nom = models.CharField(max_length=10000)







class Pays(models.Model):



    Nom = models.ManyToManyField('NomsEndroit')

    

    GPS = models.CharField(max_length=10000)



    GeoHash = models.CharField(max_length=10000)

    

    GoogleMaps = models.ManyToManyField('lien.Lien',related_name='Pays_Google',null=True,blank=True)

    

    Liens = models.ManyToManyField('lien.Lien',related_name='Pays_liens',null=True,blank=True)



class Etat(models.Model):



	Nom = models.ManyToManyField('NomsEndroit')



	GPS = models.CharField(max_length=10000)



	GeoHash = models.CharField(max_length=10000)



	GoogleMaps = models.ManyToManyField('lien.Lien',related_name='Etat_Google',null=True,blank=True)



	Liens = models.ManyToManyField('lien.Lien',related_name='Etat_liens',null=True,blank=True)



class Region(models.Model):



	Nom = models.ManyToManyField('NomsEndroit')



	GPS = models.CharField(max_length=10000)



	GeoHash = models.CharField(max_length=10000)



	GoogleMaps = models.ManyToManyField('lien.Lien',related_name='Region_Google',null=True,blank=True)



	Liens = models.ManyToManyField('lien.Lien',related_name='Region_liens',null=True,blank=True)







class Ville(models.Model):



	Nom = models.ManyToManyField('NomsEndroit')



	GPS = models.CharField(max_length=10000)



	GeoHash = models.CharField(max_length=10000)



	GoogleMaps = models.ManyToManyField('lien.Lien',related_name='Ville_Google',null=True,blank=True)



	Liens = models.ManyToManyField('lien.Lien',related_name='Ville_liens',null=True,blank=True)







class Adresse(models.Model):



	Numero = models.IntegerField(blank=True)



	Nom = models.ManyToManyField('NomsEndroit')



	GPS = models.CharField(max_length=10000)



	GeoHash = models.CharField(max_length=10000)



	GoogleMaps = models.ManyToManyField('lien.Lien',related_name='Adresse_Google',null=True,blank=True)



	Liens = models.ManyToManyField('lien.Lien',related_name='Adresse_Liens',null=True,blank=True)







class Localisation(models.Model):



	GPS = models.CharField(max_length=10000)



	GeoHash = models.CharField(max_length=10000)



	GoogleMaps = models.ManyToManyField('lien.Lien',related_name='Localisation_GoogleMaps',null=True,blank=True)



	Liens = models.ManyToManyField('lien.Lien',related_name='Localisation_Liens',null=True,blank=True)



	Adresse = models.ManyToManyField('Adresse',related_name='Localisation_Adresse')



	ville = models.ManyToManyField('Ville',related_name='Localisation_Ville')



	region = models.ManyToManyField('Region')



	etat = models.ManyToManyField('Etat')



	pays = models.ManyToManyField('pays')



	Tags = models.ManyToManyField('tag.Tag',related_name='Localisation_Liens',null=True,blank=True)




class Admin:
    pass
