from django.db import models

# Create your models here.
class Item(models.Model):  
    Nom = models.CharField(max_length=128)
    Skills = models.ManyToManyField("skill.Skill")
    Caracs = models.ManyToManyField("carac.Carac")
    Commentaire = models.TextField(max_length=256, null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return self.Nom
