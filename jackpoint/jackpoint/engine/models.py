from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CategorieNotification(models.Model):
    Nom = models.CharField(max_length=256, null=True, blank=True)

class Url(models.Model):
    Link = models.TextField(max_length=1024, null=True, blank=True)

    
class ThreadEngine(models.Model):
    Question = models.ManyToManyField('hand.Question',related_name="QuestionToThreadEngine", null=True, blank=True)
    Answer = models.ManyToManyField('hand.Answer',related_name="AnswerToThreadEngine", null=True, blank=True)
    def __unicode__(self):
        return str(self.id)


class Notification(models.Model):  
    Categorie = models.ManyToManyField('CategorieNotification', null=True, blank=True)
    ThreadEngine =  models.ManyToManyField('ThreadEngine',related_name="NotificationThreadEngine", null=True, blank=True)
    Texte = models.TextField(max_length=1024, null=True, blank=True)
    Url = models.TextField(max_length=1024, null=True, blank=True)
    Skills = models.ManyToManyField("jack.SkillUser", null=True, blank=True)
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Items = models.ManyToManyField("jack.ItemUser", null=True, blank=True)
    Caracs = models.ManyToManyField("jack.CaracUser", null=True, blank=True)
    User = models.ForeignKey(User, unique=False, null=True, blank=True,related_name="UserNotification") 
    Seen = models.BooleanField(default=False)
    #TODO
    # Why not faire le save et ecrire le texte en fonciton de la langue ?
    def __unicode__(self):
        return str(self.User.id)
    
