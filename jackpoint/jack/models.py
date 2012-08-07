from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from skill.models import Skill
class TagPrivate(models.Model):
    Tags = models.ManyToManyField("tag.Tag", blank=True, null=True)
    def __unicode__(self):
        return self.Tags
   
class ItemUser(models.Model):
    Item = models.ManyToManyField("item.Item")
    Private = models.BooleanField()

LevelSkill = (
    (0, 'None'),
    (1, 'Debutant'),
    (2, 'Moyen'),
    (3, 'Doue'),
    (4, 'Bon'),
    (5, 'Expert'),
)

class SkillUser(models.Model):
    Skill = models.ManyToManyField("skill.Skill")
    Level = models.IntegerField(choices=LevelSkill)
    Private = models.BooleanField()
    def __unicode__(self):
        Nom = ""
        for sk in self.Skill.all() :
            Nom = sk.id
        return "%s %d %r"%(Nom,self.Level,self.Private)

LevelCarac = (
    (1, 'Bof'),
    (2, 'Moyen'),
    (3, 'Pas mal'),
    (4, 'Bon'),
    (5, 'Tres Bon'),
)

class CaracUser(models.Model):
    Carac = models.ManyToManyField("carac.Carac")
    Level = models.IntegerField(choices=LevelCarac)
    Private = models.BooleanField()
    def __unicode__(self):
        #TODO
        #crade a revoir
        for c in self.carac.all() :
            t = c 
        return "%s %d %r"%(c.Nom,self.Level,self.Private)
    
    
class UserProfile(models.Model):  
    user = models.OneToOneField(User)  
    #other fields here
    Skills = models.ManyToManyField("SkillUser", blank=True, null=True)
    TagsPublic = models.ManyToManyField("tag.Tag", blank=True, null=True)
    TagsPrivate = models.ManyToManyField("TagPrivate", blank=True, null=True)
    Items = models.ManyToManyField("ItemUser", blank=True, null=True)
    Caracs = models.ManyToManyField("CaracUser", blank=True, null=True)
    Pseudo = models.CharField(max_length=256)
    Bio = models.TextField()
    Email = models.EmailField()
    Avatar = models.ImageField(upload_to='Avatar')
    Finished = models.BooleanField(default=False)
    InvitationAccepted = models.OneToOneField("invitation.Invitation",related_name="InvitationAccepted", blank=True, null=True)
    InvitationGiven = models.ManyToManyField("invitation.Invitation",related_name="InvitationGiven", blank=True, null=True)

    def __str__(self):  
          return "%s's profile" % self.user  

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 
