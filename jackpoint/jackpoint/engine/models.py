from django.db import models

# Create your models here.

class CategorieNotification(models.Model):
    Nom = models.CharField(max_length=256, null=True, blank=True)

class Url(models.Model):
    Link = models.TextField(max_length=1024, null=True, blank=True)

class Notification(models.Model):  
    Categorie = models.ManyToManyField('CategorieNotification', null=True, blank=True)
    Texte = models.TextField(max_length=256, null=True, blank=True)
    Url = models.ManyToManyField('Url',null=True, blank=True)
    Seen = models.BooleanField(default=False)
    def __unicode__(self):
        return self.Nom