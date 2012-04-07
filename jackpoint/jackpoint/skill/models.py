from django.db import models

 


class Skill(models.Model):  
    Parent = models.ManyToManyField("self",blank=True, null=True)
    Child = models.ManyToManyField("self",blank=True, null=True)
    Level = models.IntegerField()
    Nom = models.CharField(max_length=128)
    def __unicode__(self):
        return self.Nom

    
    
# Create your models here.
