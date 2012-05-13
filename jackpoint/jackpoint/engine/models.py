from django.db import models

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
    Texte = models.TextField(max_length=256, null=True, blank=True)
    Url = models.ManyToManyField('Url',null=True, blank=True)
    def __unicode__(self):
        return self.Nom
    
