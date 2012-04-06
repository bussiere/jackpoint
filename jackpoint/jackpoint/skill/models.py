from django.db import models

 


class Skill(models.Model):  
    Parent = models.ManyToManyField("self")
    Child = models.ManyToManyField("self")
    Level = models.IntegerField()
    Nom = models.CharField(max_length=128)
    
    
# Create your models here.
