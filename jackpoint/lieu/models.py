from django.db import models

# Create your models here.


class Geohash(models.Model):
    Hash = models.TextField(max_length=2048, null=True, blank=True)
    def __unicode__(self):
        return str(self.Hash)

class GPS(models.Model):
    Coord = models.TextField(max_length=2048, null=True, blank=True)
    def __unicode__(self):
        return str(self.Coord)

class Rue(models.Model): 
    GeoHash = models.ForeignKey(Geohash,null=True, blank=True)
    GPS = models.ForeignKey(GPS,null=True, blank=True)
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)

class Adresse(models.Model):
    Numero = models.TextField(max_length=1024, null=True, blank=True)
    GeoHash = models.ForeignKey(Geohash,null=True, blank=True)
    GPS = models.ForeignKey(GPS,null=True, blank=True)
    Rue = models.ForeignKey(Rue,null=True, blank=True)
    def __unicode__(self):
        return str(self.Numero + " " + self.Rue)

class CP(models.Model):
     GeoHash = models.ForeignKey(Geohash,null=True, blank=True)
     GPS = models.ForeignKey(GPS,null=True, blank=True)
     Nom = models.TextField(max_length=1024, null=True, blank=True)
     def __unicode__(self):
        return str(self.CP)




     

class Pays(models.Model):
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)

class TypeTransport(models.Model):
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)

    
class Ligne(models.Model):
    TypeTransport = models.ForeignKey(TypeTransport,null=True, blank=True)
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    def __unicode__(self):
        return str(self.TypeTransport +" "+ self.Nom)

class Region(models.Model):
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)

class Station(models.Model):
    Ligne = models.ManyToManyField(Ligne,null=True, blank=True)
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)
    
class Ville(models.Model):
    GeoHash = models.ForeignKey(Geohash,null=True, blank=True)
    GPS = models.ForeignKey(GPS,null=True, blank=True)
    Nom = models.TextField(max_length=1024, null=True, blank=True)
    def __unicode__(self):
        return str(self.Nom)

class Lieu(models.Model):
    GeoHash = models.ForeignKey(Geohash,null=True, blank=True)
    GPS = models.ForeignKey(GPS,null=True, blank=True)
    Adresse = models.ManyToManyField(Adresse,null=True, blank=True)
    Ville  = models.ForeignKey(Ville,null=True, blank=True)
    CP = models.ForeignKey(CP,null=True, blank=True)
    Region = models.ForeignKey(Region,null=True, blank=True)
    Pays = models.ForeignKey(Pays,null=True, blank=True)
    Station = models.ManyToManyField(Station,null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.GeoHash)
    
   