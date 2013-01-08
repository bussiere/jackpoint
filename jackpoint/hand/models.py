from django.db import models
from django.contrib.auth.models import User
# Create your models here.





class Question(models.Model):  
    user = models.ForeignKey(User, unique=False, null=True, blank=True)  
    #other fields here
    Skills = models.ManyToManyField("jack.SkillUser", null=True, blank=True)
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Items = models.ManyToManyField("jack.ItemUser", null=True, blank=True)
    Caracs = models.ManyToManyField("jack.CaracUser", null=True, blank=True)
    Intitule = models.TextField(null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    Url = models.TextField(null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)

class Answer(models.Model):  
    user  = models.ForeignKey(User, unique=False, null=True, blank=True)  
    Tags = models.ManyToManyField("tag.Tag", null=True, blank=True)
    Text = models.TextField(null=True, blank=True)
    Url = models.TextField(null=True, blank=True)
    Answer = models.ManyToManyField("self", related_name="AnswerToAnswer",null=True, blank=True)
    Question = models.ManyToManyField("Question", null=True, blank=True)
    Date = models.DateTimeField(auto_now_add=True, blank=True)