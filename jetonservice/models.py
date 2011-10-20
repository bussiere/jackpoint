from django.db import models



class JetonService(models.Model):

    Date = models.DateTimeField('Date visite')

    Sender = models.ManyToManyField('membre.Membre',related_name='Jeton_Sender',null=True,blank=True)

    Dest = models.ManyToManyField('membre.Membre',related_name='Jeton_Dest',null=True,blank=True)

    Object = models.CharField(max_length=800)

    Texte = models.CharField(max_length=1500)
