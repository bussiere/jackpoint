from django.db import models

# Create your models here.
class Item(models.Model):  
    Nom = models.CharField(max_length=128)
    Skills = models.ManyToManyField("skill.Skill")
    def __unicode__(self):
        return self.Nom
