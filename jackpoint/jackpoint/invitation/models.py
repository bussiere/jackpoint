from django.db import models
import random
from invitation.script import generate_invitation
# Create your models here.
class Task(models.Model):
    class Meta:
        permissions = (
            ("Create_Invitation", "Can create invitation"),
        )
    
    
class CategorieInvitation(models.Model):
    Nom = models.CharField(max_length=128, null=True, blank=True)


class Usage(models.Model):
    Nom = models.CharField(max_length=128, null=True, blank=True)

class Invitation(models.Model):   
    #other fields here
    Code = models.CharField(max_length=256, null=True, blank=True)
    Tags = models.ManyToManyField("CategorieInvitation", null=True, blank=True)
    Tags = models.ManyToManyField("Usage", null=True, blank=True)
    Note = models.TextField(max_length=256, null=True, blank=True)
    Used = models.BooleanField(default=False, blank=True)
    Donneur =  models.ManyToManyField("jack.UserProfile", related_name="DonneurInvit", null=True, blank=True)
    SendTo = models.EmailField(null=True, blank=True)
    # a revoir
    def save(self, *args, **kwargs):
        if not self.Code:
            self.Code = generate_invitation(1)[0]
            super(Invitation, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.Code

class InvitationUsed(models.Model):   
    #other fields here
    Code = models.CharField(max_length=256, null=True, blank=True)
    Tags = models.ManyToManyField("CategorieInvitation", null=True, blank=True)
    Tags = models.ManyToManyField("Usage", null=True, blank=True)
    Note = models.TextField(max_length=256, null=True, blank=True)
    SendTo = models.EmailField(null=True, blank=True)
    Receveur = models.ManyToManyField("jack.UserProfile", related_name="ReceveurINvit",null=True, blank=True)
    Donneur =  models.ManyToManyField("jack.UserProfile", related_name="DonneurINvitUsed", null=True, blank=True)
    def __unicode__(self):
        return self.Code
    # a revoir


    