from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CategorieNotification(models.Model):  
    Nom = models.CharField(max_length=128)
    Commentaire = models.TextField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.Nom

class Notification(models.Model):  
    user = models.OneToOneField(User)  
    Nom = models.CharField(max_length=128)
    Texte = models.TextField(max_length=256, null=True, blank=True)
    hand = models.ManyToManyField("hand.Question", blank=True, null=True)
    Commentaire = models.TextField(max_length=256, null=True, blank=True)
    def __unicode__(self):
        return self.Nom
