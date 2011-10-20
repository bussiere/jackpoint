from django.db import models



# Create your models here.



Notation = (

    (0, 'Vierge'),

    (1, 'Cree'),

    (2, 'Utilisee'),



)

class Invitation(models.Model):
    
    Createur = models.ManyToManyField('membre.Membre',related_name='Invit_Createur',null=True,blank=True)

    Receveur = models.ManyToManyField('membre.Membre',related_name='Invit_Receveur',null=True,blank=True)

    Code = models.CharField(max_length=1500)

    Statut = models.IntegerField(max_length=1, choices=Notation,blank=True)
