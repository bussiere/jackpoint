from django.db import models



# Create your models here.



Notation = (

    (1, 'Nul'),

    (2, 'A peine passable'),

    (3, 'Moyen'),

    (4, 'Bien'),

    (5, 'Tres bien'),



)

class Notation(models.Model):

        Notation = models.IntegerField(max_length=1, choices=Notation,blank=True)

        Membre = models.ManyToManyField('membre.Membre')
