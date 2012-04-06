from django.db import models

class Carac (models.Model):  
    Nom = models.CharField(max_length=64, null=True, blank=True)
