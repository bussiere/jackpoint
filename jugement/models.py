from django.db import models





class NoteBoulet(models.Model):

    NoteBoulet = models.FloatField()



class NoteDangerosite(models.Model):

    NoteDangerosite = models.FloatField()



class Jugement(models.Model):

    Date = models.DateTimeField('Date visite',null=True,blank=True)

    Sender = models.ManyToManyField('membre.Membre',related_name='Jugement_Sender',null=True,blank=True)

    Dest = models.ManyToManyField('membre.Membre',related_name='Jugement_Dest',null=True,blank=True)

    NoteBoulet = models.ManyToManyField(NoteBoulet)

    NoteDangerosite = models.ManyToManyField(NoteDangerosite)

    Object = models.CharField(max_length=800)

    Texte = models.CharField(max_length=1500)

    Visiblite = models.ManyToManyField('visibilite.Visibilite',null=True,blank=True)

# Create your models here.

