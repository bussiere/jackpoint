from django.db import models

class Carac (models.Model):  
    Nom = models.CharField(max_length=64, null=True, blank=True)
    Commentaire = models.TextField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.Nom
