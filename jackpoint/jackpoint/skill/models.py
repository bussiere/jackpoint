from django.db import models

 


class Skill(models.Model):  
    Parent = models.ManyToManyField("self",blank=True, null=True)
    Child = models.ManyToManyField("self",blank=True, null=True)
    Level = models.IntegerField()
    Nom = models.CharField(max_length=128)
    
    
# Create your models here.
